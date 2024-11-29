
def is_nested(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    is_nested('[[]]') ➞ True
    is_nested('[]]]]]]][[[[[]') ➞ False
    is_nested('[][]') ➞ False
    is_nested('[]') ➞ False
    is_nested('[[][]]') ➞ True
    is_nested('[[]][[') ➞ True
    '''

    stack = []
    nested = False
    
    for char in string:
        if char == '[':
            stack.append(char)
            if len(stack) > 1:
                nested = True
        elif char == ']':
            if not stack:
                return False
            stack.pop()
    
    return nested and not stack
    stack = []
    nested = False
    
    for char in string:
        if char == '[':
            stack.append(char)
            if len(stack) > 1:  # More than one '[' indicates nesting
                nested = True
        elif char == ']':
            if not stack:
                return False  # Unmatched closing bracket
            stack.pop()
    
    return nested and not stack
def check(candidate):

    # Check some simple cases
    assert candidate('[[]]') == True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate('[]]]]]]][[[[[]') == False
    assert candidate('[][]') == False
    assert candidate(('[]')) == False
    assert candidate('[[[[]]]]') == True

    # Check some edge cases that are easy to work out by hand.


check(is_nested)