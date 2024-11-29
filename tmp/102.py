def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return ''.join(x.capitalize() for x in components)
assert snake_to_camel('python_program')=='PythonProgram'
assert snake_to_camel('python_language')==('PythonLanguage')
assert snake_to_camel('programming_language')==('ProgrammingLanguage')