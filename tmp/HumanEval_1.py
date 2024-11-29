from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    paren_string = paren_string.replace(' ', '')
    groups = []
    current_group = []
    balance = 0
    
    for char in paren_string:
        if char == '(':
            if balance == 0 and current_group:
                groups.append(''.join(current_group))
                current_group = []
            current_group.append(char)
            balance += 1
        elif char == ')':
            current_group.append(char)
            balance -= 1
            if balance == 0:
                groups.append(''.join(current_group))
                current_group = []
    
    return groups
    paren_string = paren_string.replace(" ", "")
    result = []
    current_group = ""
    balance = 0

    for char in paren_string:
        current_group += char
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
        
        if balance == 0:
            result.append(current_group)
            current_group = ""

    return result


METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('(()()) ((())) () ((())()())') == [
        '(()())', '((()))', '()', '((())()())'
    ]
        '()', '(())', '((()))', '(((())))'
    ]
        '(()(())((())))'
    ]

check(separate_paren_groups)