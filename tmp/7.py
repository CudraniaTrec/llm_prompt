def find_char_long(input_string):
    words = input_string.split()
    long_words = [word for word in words if len(word) >= 4]
    return long_words
assert set(find_char_long('Please move back to stream')) == set(['Please', 'move', 'back', 'stream'])
assert set(find_char_long('Jing Eco and Tech')) == set(['Jing', 'Tech'])
assert set(find_char_long('Jhingai wulu road Zone 3')) == set(['Jhingai', 'wulu', 'road', 'Zone'])