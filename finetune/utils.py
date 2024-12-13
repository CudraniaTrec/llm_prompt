import pandas as pd
import json, signal
from tqdm import tqdm
import torch, os
from transformers import AutoTokenizer, AutoModelForCausalLM
import multiprocessing as mp
import subprocess
import random, numpy as np

# dump results to csv
def dump_results(dataset, model, method, tot, faillist):
    results = pd.read_csv('results.csv',index_col="name")
    res_row_name = f"{dataset}__{model}__{method}" if method else f"{dataset}__{model}"
    res_correct = tot - len(faillist)
    res_accuracy = f"{res_correct / tot:.2%}"
    results.loc[res_row_name, :] = [tot, res_correct, res_accuracy]
    results.to_csv('results.csv', index=True)

# find the path of the dataset
def find_data_path(dataset):
    if dataset == "mbpp":
        data_path = "../prompt/datasets/sanitized-mbpp.json"
    elif dataset == "humaneval":
        data_path = "../prompt/datasets/HumanEval.json"
    elif dataset == "mathqa":
        data_path = "../prompt/datasets/mathqa-python-test.json"
    else:
        raise ValueError("Invalid dataset: "+dataset)
    return data_path

# find check point for the model
def find_checkpoint(model):
    if model == "starcoder-3b":
        checkpoint = "bigcode/starcoder2-3b"
    elif model == "codellama-instruct":
        checkpoint = "codellama/CodeLlama-7b-Instruct-hf"
    elif model == "codellama-python":
        checkpoint = "codellama/CodeLlama-7b-Python-hf"
    elif model == "qwen1.5":
        checkpoint = "Qwen/Qwen2.5-1.5B-Instruct"
    elif model == "opencoder1.5":
        checkpoint = "infly/OpenCoder-1.5B-Instruct"
    else:
        raise ValueError("Invalid model: "+model)
    return checkpoint

# examine the correctness of the generated code
def complete_code(code,problem,dataset, test_num=5):
    if dataset == "mbpp":
        for test_import in problem['test_imports']:
            code = test_import + "\n" + code
        for test_case in problem['test_list'][:test_num]:
            code += "\n" + test_case
    elif dataset == "humaneval":
        tests = problem['test'].split("\n")
        new_tests = []
        for test in tests:
            if "assert" in test:
                if test_num>0:
                    new_tests.append(test)
                    test_num -= 1
            else:
                new_tests.append(test)
        new_tests = "\n".join(new_tests)
        if f"def {problem['entry_point']}(" in code:
            code += f"\n{new_tests}\ncheck({problem['entry_point']})"
        else:
            code = problem['prompt'] + "\n" + code + f"\n{new_tests}\ncheck({problem['entry_point']})"
    elif dataset == "mathqa":
        code += f"\nassert answer == {problem['answer']}"
    else:
        raise ValueError("Invalid dataset: "+dataset)
    code = "\n".join([line for line in code.splitlines() if line.strip()])
    return code

def test_correctness(dataset, problem, code, verbose=False):
    code = complete_code(code, problem, dataset)
    #try to run the code

    # set up the timeout
    def handler(signum, frame):
        raise Exception("timeout")
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(5)
    try:
        p = subprocess.run(['python', '-c', code],
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               timeout=5)
        if p.returncode != 0:
            if verbose:
                print("Failed to run the code:")
                print(p.stderr.decode())
                print(code)
            return False
    except Exception as e:
        if verbose:
            print("Timeout:")
            print(code)
        return False
    finally:
        signal.alarm(0)
    return True

# code generation for the given dataset
def codegen_direct(model, dataset, get_input, process_output):
    """
    Generate code for the given dataset using the given model
    model: starcoder-3b, codellama-instruct, codellama-python, qwen1.5, opencoder1.5
    dataset: mbpp, humaneval, mathqa
    """
    model_name = model
    checkpoint = find_checkpoint(model)
    tokenizer = AutoTokenizer.from_pretrained(checkpoint,
                                              use_fast=True,
                                              trust_remote_code=True,
                                              local_files_only=True)
    if not tokenizer.pad_token:
        tokenizer.pad_token = tokenizer.eos_token
    model = AutoModelForCausalLM.from_pretrained(checkpoint, 
                                             device_map="auto",
                                             local_files_only=True,
                                             trust_remote_code=True,
                                             torch_dtype=torch.bfloat16)

    def codegen_batch(problems):
        questions = [get_input(problem,dataset,tokenizer) for problem in problems]
        inputs = tokenizer(questions,
                           padding=True,
                           padding_side="left",
                           truncation=True,
                           max_length=1024,
                           return_tensors="pt").to("cuda")
        with torch.no_grad():
            outputs = model.generate(**inputs,
                                     pad_token_id=tokenizer.pad_token_id,
                                     max_new_tokens=1024,
                                     do_sample=False)
        failed_list = []
        for i, problem in enumerate(problems):
            output = tokenizer.decode(outputs[i], skip_special_tokens=True)
            code = process_output(output, tokenizer)
            if not test_correctness(dataset, problem, code, verbose=False):
                failed_list.append(problem["task_id"])
        return failed_list

    datapath = find_data_path(dataset)
    problems = json.load(open(datapath))
    fail_list = []
    batch_size = 20
    with tqdm(total=len(problems)) as pbar:
        for i in range(0, len(problems), batch_size):
            res = codegen_batch(problems[i:i+batch_size])
            fail_list += res
            pbar.update(batch_size)
            pbar.set_postfix({"failed": len(fail_list)})
    print(f"Failed {len(fail_list)} out of {len(problems)} problems:")
    dump_results(dataset, model_name, "", len(problems), fail_list)

# set seed for reproducibility
def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)