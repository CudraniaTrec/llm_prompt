from openai import OpenAI
import json, beeprint
from tqdm import tqdm
import signal
import pandas as pd

client = OpenAI(
        **json.load(open('apikey.json'))["closeai"]
    )

# dataset: mbpp, humaneval, mathqa
# model: gpt-3.5-turbo, gpt-4o-mini, o1-mini，claude-3-5-sonnet-latest 

# dump results to csv
def dump_results(dataset, model, method, tot, faillist):
    results = pd.read_csv('results.csv',index_col="name")
    res_row_name = f"{dataset}__{model}__{method}" if method else f"{dataset}__{model}"
    res_correct = tot - len(faillist)
    res_accuracy = f"{res_correct / tot:.2%}"
    results.loc[res_row_name, :] = [tot, res_correct, res_accuracy]
    results.to_csv('results.csv', index=True)

# examine the correctness of the code
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
        signal.alarm(5)  # Set the timeout to 5 seconds
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

# ask llm to generate code directly
def codegen_direct(model="gpt-4o-mini", dataset="mbpp"):
    def codegen_one(problem):
        if dataset == "mbpp":
            question = "Write a python program to solve the following problem:\n"
            question += problem['prompt']
            question += "\nYour code should be able to solve the following test cases:\n"
            question += problem['test_list'][0]
        elif dataset == "humaneval":
            question = "Complete the following python code, according to the docstring:\n"
            question += problem['prompt']
            question += "\nMethod header is given in the prompt, you only need to provide method body\n"
        elif dataset == "mathqa":
            question = "Write a python program to solve the following math problem:\n"
            question += problem['text']
            question += "\nYou don't have to define any functions or methods, just name the final result variable as `answer`:\n"
        question += "\nOnly the code is needed, no explanation, no example usage"
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": question,
                }
            ],
            model=model,
        )
        code = response.choices[0].message.content
        ## if the code is wrapped in markdown, remove it
        if code.startswith("```") and code.endswith("```"):
            lines = code.splitlines()[1:-1]
            code = "\n".join(lines)
        return test_correctness(dataset, problem, code)

    if dataset == "mbpp":
        datapath = f"datasets/sanitized-mbpp.json"
    elif dataset == "humaneval":
        datapath = f"datasets/HumanEval.json"
    elif dataset == "mathqa":
        datapath = f"datasets/mathqa-python-test.json"
    else:
        raise ValueError("Invalid dataset: "+dataset)
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

# ask llm to generate code line by line
# method: intermediate, simple
def codegen_by_line_one(problem, dataset="mbpp", model="gpt-4o-mini", method="simple"):
    def eval_partial_code(ans, problem, test_num=5):
        code = '\n'.join(ans)
        code = complete_code(code, problem, dataset, test_num)
        #try to run the code
        try:
            import subprocess
            file_name = f"tmp/{problem['task_id'].replace("/","_")}.py"
            with open(file_name, "w") as f:
                f.write(code)
            res = subprocess.run(["python", "intermediate.py", file_name], timeout=5,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if res.returncode!=0:
                return False, res.stderr.decode()
            else:
                return True, res.stdout.decode()
        except Exception as e:
            return False, f"\nError in Solving Problem{problem['task_id']}: {e}"

    max_lines = 30
    ans = [] if dataset == "mbpp" else problem['prompt'].split("\n")
    added_question = ""
    while True:
        if dataset == "mbpp":
            question = "Task: Write a python program line by line based on existed partial code to solve the following problem:\n"
            question += problem['prompt']+ "\n"
            question += "Example: Your code should be able to solve the following test cases:\n"
            question += problem['test_list'][0]+ "\n"
            question += "Partial Code: Here is the partial code(empty means you need to start writing the first line):\n"
            question += "```python\n"+'\n'.join(ans)+"\n```\n"
        elif dataset == "humaneval":
            question = "Complete the following python partial program, according to the docstring:\n"
            question += problem['prompt']+ "\n"
            question += "You only need to continue with existing partial code and provide the rest of the method body\n"
        else:
            raise ValueError("Invalid dataset: "+dataset)
        question += "Hint: If you believe the above code is completed, please output ##end##, don't give redunt line or redunt method\n"
        question += "Only lines of code is needed, no explanation, no example usage\n"
        question += added_question
        added_question = ""
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": question,
                }
            ],
            model=model,
        )
        code = response.choices[0].message.content
        ## if the code is wrapped in markdown, remove it
        while code.startswith("```") and code.endswith("```"):
            lines = code.splitlines()[1:-1]
            code = "\n".join(lines)
        # answer is too long
        max_lines -= 1
        if max_lines < 0:
            break
        # gpt says is done
        if '##end##' in code:
            if method != "simple" and len(ans)<=1:
                continue
            break
        
        if f"def {problem['entry_point']}(" in code:
            ans=code.splitlines()
        else:
            ans+=code.splitlines()
        if method == "intermediate":
            _, output = eval_partial_code(ans, problem, test_num=1)
            output = output[-100000:]
            added_question += "Live execution results for current code: \n"
            added_question += f"{output}\n"

    res, _ = eval_partial_code(ans, problem)
    return res

def codegen_by_line(model="gpt-4o-mini", method="simple", dataset="mbpp",parallel=False):
    data_path = f"datasets/{'sanitized-mbpp' if dataset=='mbpp' else 'HumanEval'}.json"
    problems = json.load(open(data_path))[:500]
    if parallel:
        from multiprocessing import Pool
        with tqdm(total=len(problems)) as pbar:
            fail_num=0
            def callback(x):
                nonlocal fail_num
                if not x:
                    fail_num+=1
                pbar.update(1)
                pbar.set_postfix({"failed": fail_num})
            with Pool(20) as pool:
                res = [pool.apply_async(codegen_by_line_one, (problem,dataset,model,method), callback=callback) 
                       for problem in problems]
                res = [r.get() for r in res]
        fail_list = [problem["task_id"] for problem, r in zip(problems, res) if not r]
    else:
        fail_list = []
        with tqdm(total=len(problems)) as pbar:
            for problem in problems:
                try:
                    if not codegen_by_line_one(problem=problem, dataset=dataset, model=model, method=method):
                        fail_list.append(problem["task_id"])
                except Exception as e:
                    print(f"\nError in Solving Problem{problem['task_id']}: {e}")
                    fail_list.append(problem["task_id"])
                pbar.update(1)
                pbar.set_postfix({"failed": len(fail_list)})
    # dump results to csv
    dump_results(dataset, model, method, len(problems), fail_list)

if __name__ == '__main__':
    codegen_direct(model="gpt-4o-mini", dataset="mathqa")
    # codegen_by_line(model="gpt-4o-mini", method="intermediate", dataset="humaneval",parallel=True)
