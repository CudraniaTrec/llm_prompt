def occurance_substring(input_string, substring):
    start = input_string.find(substring)
    if start == -1:
        return None
    end = start + len(substring) - 1
    return (substring, start, end)
assert occurance_substring('python programming, python language','python')==('python', 0, 6)
assert occurance_substring('python programming,programming language','programming')==('programming', 7, 18)
assert occurance_substring('python programming,programming language','language')==('language', 31, 39)
assert occurance_substring('c++ programming, c++ language','python')==None