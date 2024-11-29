import sys
import inspect

start_filename = "tmp.py"

def process_variable(var):
    type_name = type(var).__name__
    if type_name == 'list':
        return format_list(var)
    elif type_name == 'module':
        return "<module '%s'>" % var.__name__
    elif type_name == 'function':
        info = inspect.signature(var)
        return f"<function {var.__name__}{info}>"
    else:
        return str(var)

def truncate_list(l):
    if len(l) > 3:
        ret = ', '.join(map(process_variable, l[:2]))
        ret += ", ..., "
        ret += process_variable(l[-1])
        return ret
    else:
        return ', '.join(map(process_variable, l))

def format_list(l):
    return "[%s]" % truncate_list(l)
    
def should_ignore_variable(name):
    return name.startswith('__') and name.endswith('__')

def trace_lines(frame, event, arg):
    if event != 'line': # only trace line events
        return
    
    # 获取当前帧的局部变量,排除掉隐藏的变量
    frame_locals = {k:
       {'value': process_variable(v), 'type': type(v).__name__}
       for k, v in frame.f_locals.items() if not should_ignore_variable(k)
    }
    frame_globals = {k:
       {'value': process_variable(v), 'type': type(v).__name__}
       for k, v in frame.f_globals.items() if not should_ignore_variable(k)
    }
    # 获取当前行号
    lineno = frame.f_lineno
    # 获取当前文件名
    filename = frame.f_code.co_filename
    # 获取当前函数名
    func_name = frame.f_code.co_name
    # 获取当前代码行
    frame_info = inspect.getframeinfo(frame)
    code_line = frame_info.code_context[0].strip()

    if filename != start_filename:
        return
    if "import" in code_line:
        return

    print(f"Line {lineno} in {func_name} ({filename}): {code_line}")
    print("Variables:")
    for var_name, var_value in frame_locals.items():
        print(f"  {var_name}: {var_value}")
    print("-" * 40)

def trace(frame, event, arg):
    # 获取当前代码行
    frame_info = inspect.getframeinfo(frame)
    file_name = frame_info.filename
    if file_name != start_filename:
        return
    return trace_lines

namespace = {
    '__file__': start_filename,
    '__name__': '__main__',
}

with open(start_filename, 'r') as f:
    code = f.read()

sys.settrace(trace)
code = compile(code, start_filename, 'exec')
exec(code, namespace)
sys.settrace(None)