import pandas as pd
import json, signal
from tqdm import tqdm
import torch, os
from transformers import AutoTokenizer, AutoModelForCausalLM

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
    return code

def test_correctness(dataset, problem, code):
    code = complete_code(code, problem, dataset)
    #try to run the code
    try:
        def handler(signum, frame):
            raise TimeoutError("Execution timed out")
        signal.signal(signal.SIGALRM, handler)
        signal.alarm(1)  # Set the timeout to 1 seconds
        try:
            namespace = {
                '__file__': f"tmp/{problem['task_id']}.py",
                '__name__': '__main__',
            }
            exec(code, namespace)
        finally:
            signal.alarm(0)  # Disable the alarm
        return True
    except Exception as e:
        # print(code)
        # print(f"\nError in Solving Problem {problem['task_id']}: {e}")
        return False

def codegen_direct(model="starcoder-3b", dataset="mbpp"):
    """
    Generate code for the given dataset using the given model
    model: starcoder-3b, codellama-instruct, codellama-python
    dataset: mbpp, humaneval, mathqa
    """
    checkpoint = find_checkpoint(model)
    tokenizer = AutoTokenizer.from_pretrained(checkpoint)
    # for fp16 use `torch_dtype=torch.float16` instead
    model = AutoModelForCausalLM.from_pretrained(checkpoint, device_map="auto", torch_dtype=torch.bfloat16)

    def codegen_one(problem):
        if dataset == "mbpp":
            question = "Write a python program to solve the following problem:\n"
            question += problem['prompt']
            question += "\nYour code should be able to solve the following test cases:\n"
            question += "\n".join(problem['test_list'])+ "\n"
        elif dataset == "humaneval":
            question = "Complete the following python code, according to the docstring:\n"
            question += problem['prompt']
            question += "\nMethod header is given in the prompt, you only need to provide method body\n"
        elif dataset == "mathqa":
            question = "Write a python program to solve the following math problem:\n"
            question += problem['text']
            question += "\nYou don't have to define any functions or methods, just name the final result variable as `answer`:\n"
        question += "\nOnly the code is needed, no explanation, no example usage"

        inputs = tokenizer.encode(question, return_tensors="pt").to("cuda")
        outputs = model.generate(inputs)
        code = tokenizer.decode(outputs[0])
        ## if the code is wrapped in markdown, remove it
        if code.startswith("```") and code.endswith("```"):
            lines = code.splitlines()[1:-1]
            code = "\n".join(lines)
        return test_correctness(dataset, problem, code)

    datapath = find_data_path(dataset)
    problems = json.load(open(datapath))[:500]
    fail_list = []
    with tqdm(total=len(problems)) as pbar:
        for problem in problems:
            try:
                if not codegen_one(problem):
                    fail_list.append(problem["task_id"])
            except Exception as e:
                print(f"\nError in Solving Problem {problem['task_id']}: {e}")
                fail_list.append(problem["task_id"])
            pbar.update(1)
            pbar.set_postfix({"failed": len(fail_list)})

    print(f"Failed {len(fail_list)} out of {len(problems)} problems:")
    dump_results(dataset, model, "", len(problems), fail_list)