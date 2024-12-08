import pandas as pd
import json, signal
from tqdm import tqdm
import torch, os
from transformers import AutoTokenizer, AutoModelForCausalLM
import multiprocessing as mp
import subprocess

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
    return True
    
def codegen_direct(model="codellama-instruct", dataset="mbpp"):
    """
    Generate code for the given dataset using the given model
    model: starcoder-3b, codellama-instruct, codellama-python
    dataset: mbpp, humaneval, mathqa
    """
    model_name = model
    checkpoint = find_checkpoint(model)
    tokenizer = AutoTokenizer.from_pretrained(checkpoint, use_fast=True, local_files_only=True)
    tokenizer.pad_token = tokenizer.eos_token
    # for fp16 use `torch_dtype=torch.float16` instead
    model = AutoModelForCausalLM.from_pretrained(checkpoint, 
                                             device_map="auto",
                                             local_files_only=True, 
                                             torch_dtype=torch.bfloat16)

    def codegen_batch(problems):
        def getinput(problem):
            if dataset == "mbpp":
                question = "Complete the following task in Python.\n"
                question += problem['prompt']
                question += "\nPlease respond with code only, no explanations, no example IOs, no annotations and no print statements.\n"
                question += "\nYour code should be able to solve the following test cases:\n"
                question += "\n".join(problem['test_list'])
                # add # to the beginning of each line
                question = "\n".join(["# "+line for line in question.splitlines()])
                question += "\ndef"

            elif dataset == "humaneval":
                question = "# Complete the following python code, according to the docstring:\n"
                question += "\n# Please respond with code only, no explanations, no example IOs, no annotations and no print statements.\n"
                question += problem['prompt']

            elif dataset == "mathqa":
                question = "Write a python program to solve the following math problem:\n"
                question += problem['text']
                question += "\nYou don't have to define any functions or methods, just name the final result variable as `answer`:\n"
            else:
                raise ValueError("Invalid dataset: "+dataset)
            return question
        def process_output(code):
            if code.startswith("```") and code.endswith("```"):
                code = "\n".join(code.splitlines()[1:-1])
            code = code.replace(tokenizer.bos_token, "").replace(tokenizer.eos_token, "")
            # remove replicated \n
            code = "\n".join([line for line in code.splitlines() if line.strip()])
            return code
        
        questions = [getinput(problem) for problem in problems]
        inputs = tokenizer(questions, 
                           return_tensors="pt", 
                           padding=True, 
                           truncation=True,
                           max_length=768)
        # print input length
        # print("Input length: ", inputs["input_ids"].shape[1])
        inputs = {k: v.to("cuda") for k, v in inputs.items()}
        with torch.no_grad():
            outputs = model.generate(**inputs, 
                            pad_token_id=tokenizer.eos_token_id,
                            max_length=1024)
        failed_list = []
        for i, problem in enumerate(problems):
            code = process_output(tokenizer.decode(outputs[i]))
            if not test_correctness(dataset, problem, code, verbose=False):
                failed_list.append(problem["task_id"])
        return failed_list

    datapath = find_data_path(dataset)
    problems = json.load(open(datapath))[:500]
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