def check_expression(expression):
    stack = []
    opening = set('({[')
    matching = {')': '(', '}': '{', ']': '['}
    
    for char in expression:
        if char in opening:
            stack.append(char)
        elif char in matching:
            if not stack or stack.pop() != matching[char]:
                return False
            
    return len(stack) == 0
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{]") == False
assert check_expression("{()}[{}][]({})") == True