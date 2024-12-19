import pandas as pd
import json, signal

from tqdm import tqdm
import torch, os
from transformers import AutoTokenizer, AutoModelForCausalLM
from datasets import load_dataset
import subprocess
import random, numpy as np

config = {
    "max_input_length": 1024,
    "max_output_length": 512,
    'batch_size': 40,
    'seed': 321876902
}

# dump results to csv
def dump_results(dataset, model, method, tot, faillist):
    results = pd.read_csv('results.csv',index_col="name")
    res_row_name = f"{dataset}__{model}__{method}" if method else f"{dataset}__{model}"
    res_correct = tot - len(faillist)
    res_accuracy = f"{res_correct / tot:.2%}"
    print(f"Results for {res_row_name}: {res_correct}/{tot} ({res_accuracy})")
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

# load and split the dataset
def prepare_data(dataset_name):
    if dataset_name == "mbpp":
        # dataset = find_data_path("mbpp")
        # data = json.load(open(dataset))
        # def store_split(s):
        #     with open(f"tmp/mbpp_{s}.json", "w") as f:
        #         json.dump([d for d in data if d['split']==s], f, indent=2)
        # for s in ['prompt', 'train', 'validation', 'test']:
        #     store_split(s)
        return load_dataset('json', data_files={'test': 'tmp/mbpp_test.json',
                                                'train': 'tmp/mbpp_train.json',
                                                'valid': 'tmp/mbpp_validation.json',
                                                'prompt': 'tmp/mbpp_prompt.json'})
    elif dataset_name == "humaneval":
        dataset = find_data_path("humaneval")
        return load_dataset('json', data_files={'test': dataset})
    elif dataset_name == "mathqa":
        test_dataset = find_data_path("mathqa")
        train_dataset = test_dataset.replace("test", "train")
        print(test_dataset, train_dataset)
        return load_dataset('json', data_files={'test': test_dataset,
                                                'train': train_dataset})
    else:
        raise ValueError("Invalid dataset: "+dataset_name)

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
    elif model == "qwen7":
        checkpoint = "Qwen/Qwen2.5-7B-Instruct"
    elif model == "opencoder1.5":
        checkpoint = "infly/OpenCoder-1.5B-Instruct"
    elif model == "opencoder8":
        checkpoint = "infly/OpenCoder-8B-Instruct"
    else:
        raise ValueError("Invalid model: "+model)
    return checkpoint

# complete the generated code with the test cases
def complete_code(code, problem, dataset, test_num=10):
    if dataset == "mbpp":
        for test_import in problem['test_imports']:
            code = test_import + "\n" + code
        for test_case in problem['test_list'][:test_num]:
            code += "\n" + test_case
    elif dataset == "humaneval":
        tests = problem['test']
        # remove metadata definition
        if "METADATA" in tests:
            start_idx = tests.index("METADATA")
            end_idx = tests.index("}", start_idx)
            tests = tests[:start_idx] + tests[end_idx+1:]
        new_tests = []
        for test in tests.split("\n"):
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

    # remove multiline comments
    while "'''" in code:
        start_idx = code.index("'''")
        end_idx = code.index("'''", start_idx + 3)
        code = code[:start_idx] + code[end_idx+3:]
    while '"""' in code:
        start_idx = code.index('"""')
        end_idx = code.index('"""', start_idx + 3)
        code = code[:start_idx] + code[end_idx+3:]

    # remove empty lines and annotations
    code = "\n".join([line for line in code.splitlines() if line.strip() and not line.strip().startswith("#")])
    return code

# examine the correctness of the generated code
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
                print('='*20)
                print("Failed to run the code:")
                print(p.stderr.decode())
                print(code)
            return False
    except Exception as e:
        if verbose:
            print('='*20)
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
                           max_length=config["max_input_length"],
                           return_tensors="pt").to("cuda")
        with torch.no_grad():
            outputs = model.generate(**inputs,
                                     pad_token_id=tokenizer.pad_token_id,
                                     max_new_tokens=config["max_output_length"],)
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
    batch_size = config['batch_size']
    with tqdm(total=len(problems)) as pbar:
        for i in range(0, len(problems), batch_size):
            res = codegen_batch(problems[i:i+batch_size])
            fail_list += res
            pbar.update(batch_size)
            pbar.set_postfix({"failed": len(fail_list)})
    dump_results(dataset, model_name, "", len(problems), fail_list)

# set seed for reproducibility
def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)

def print_special_tokens(tokenizer):
    print("Special tokens:")
    print(tokenizer.special_tokens_map)
    for token_name, token in tokenizer.special_tokens_map.items():
        token_id = tokenizer.convert_tokens_to_ids(token)
        print(f"{token_name}: '{token}' (ID: {token_id})")


