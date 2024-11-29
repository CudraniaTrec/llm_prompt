def remove_parenthesis(strings):
    return [s.split('(')[0].strip() for s in strings]
assert remove_parenthesis(["python (chrome)"])==("python")
assert remove_parenthesis(["string(.abc)"])==("string")
assert remove_parenthesis(["alpha(num)"])==("alpha")