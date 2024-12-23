import ast

def has_recursive_call(code):
    """
    检查给定的 Python 源代码是否包含递归调用。
    :param code: str, Python 源代码
    :return: list, 包含递归调用的函数名称（如果没有递归调用，则返回空列表）
    """
    class RecursiveCallChecker(ast.NodeVisitor):
        def __init__(self):
            self.current_function = None  # 当前正在检查的函数名称
            self.recursive_functions = set()  # 存储有递归调用的函数名

        def visit_FunctionDef(self, node):
            """
            处理函数定义语句。
            """
            self.current_function = node.name
            # 检查函数体
            self.generic_visit(node)
            self.current_function = None

        def visit_Call(self, node):
            """
            处理函数调用语句。
            """
            # 检查调用的函数是否是当前函数本身（递归调用）
            if isinstance(node.func, ast.Name) and node.func.id == self.current_function:
                self.recursive_functions.add(self.current_function)
            self.generic_visit(node)  # 继续检查其他节点

    # 解析代码并检查递归调用
    tree = ast.parse(code)
    checker = RecursiveCallChecker()
    checker.visit(tree)

    return list(checker.recursive_functions)

def has_loop_in_code(code):
    """
    检查Python代码中是否有循环
    :param code: str, 待检查的Python代码
    :return: bool, 是否有循环
    """
    try:
        # 将代码解析为AST（抽象语法树）
        tree = ast.parse(code)

        # 遍历AST树
        for node in ast.walk(tree):
            # 检查是否有For或While节点
            if isinstance(node, (ast.For, ast.While)):
                return True

        return False
    except SyntaxError as e:
        print(f"代码解析错误: {e}")
        return False


# 示例用法
if __name__ == "__main__":
    # 示例代码段
    example_code = """
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def add(a, b):
    return a + b

def non_recursive():
    return "Hello, world!"

def indirect_recursion_a(x):
    return indirect_recursion_b(x - 1)

def indirect_recursion_b(x):
    return indirect_recursion_a(x + 1)
"""
    # 判断是否有递归调用
    recursive_functions = has_recursive_call(example_code)
    if recursive_functions:
        print(f"递归调用的函数有: {recursive_functions}")
    else:
        print("没有递归调用的函数。")