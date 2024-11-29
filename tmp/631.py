def replace_spaces(input_string):
    result = ''
    for char in input_string:
        if char == ' ':
            result += '_'
        elif char == '_':
            result += ' '
        else:
            result += char
    return result
assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'
assert replace_spaces('The_Avengers') == 'The Avengers'
assert replace_spaces('Fast and Furious') == 'Fast_and_Furious'