def capital_words_spaces(s):
    result = ''
    for char in s:
        if char.isupper() and result: 
            result += ' ' 
        result += char
    return result
assert capital_words_spaces("Python") == 'Python'
assert capital_words_spaces("PythonProgrammingExamples") == 'Python Programming Examples'
assert capital_words_spaces("GetReadyToBeCodingFreak") == 'Get Ready To Be Coding Freak'