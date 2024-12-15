from utils import complete_code, find_data_path
import re, traceback, json

# annotate a (partial) python program with its trace information
def annotate(code, problem, dataset):
    code = complete_code(code, problem, dataset, test_num=1)
    print(code+'\n')
    code_lines = [ [line] for line in code.split('\n')]
    with open('tmp.py', 'w') as f:
        f.write(code)
    import subprocess
    try:
        p = subprocess.run(['python', '-m', 'trace', 'tmp.py'],
                           stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           timeout=5)
        if p.returncode == 0:
            traces = p.stdout.decode('utf-8')
        else:
            raise Exception(p.stderr.decode('utf-8'))

        steps = traces.split("-" * 50)
        for step in steps:
            try:
                step_info = json.loads(step)
            except:
                continue
            step_no= step_info['step_no']
            line_no = step_info['line_no']
            func_name = step_info['func_name']
            code_lines_step = code_lines[int(line_no) - 1]
            var_info = [f"{var_name}={var_value['value']}" for var_name, var_value in step_info['frame_locals'].items()]
            code_lines_step.append(f"# Step {step_no}: {'; '.join(var_info)}")
            code_lines[int(line_no) - 1] = code_lines_step

        for i in range(len(code_lines)):
            code_lines_step = code_lines[i]
            origin_line = code_lines_step[0]
            traces = code_lines_step[1:]
            if len(traces) > 3:
                traces = traces[:2] + ['...'] + traces[-1:]
            code_lines[i] = "\n".join(traces+[origin_line])
        return "\n\n".join(code_lines)
    except Exception as e:
        print(e)
        return ""

if __name__ == '__main__':
    data_path = find_data_path("humaneval")
    with open(data_path) as f:
        datas = json.load(f)
    problem = datas[0]
    code = problem['canonical_solution']
    code = '\n'.join(code.split('\n')[:-2])
    print(annotate(code, problem, 'humaneval'))