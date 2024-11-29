def odd_values_string(s):
    return ''.join(s[i] for i in range(len(s)) if i % 2 == 0)
assert odd_values_string('abcdef') == 'ace'
assert odd_values_string('python') == 'pto'
assert odd_values_string('data') == 'dt'
assert odd_values_string('lambs') == 'lms'