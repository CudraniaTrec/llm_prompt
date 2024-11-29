def first_repeated_char(s):
    char_set = set()
    for char in s:
        if char in char_set:
            return char
        char_set.add(char)
    return None
def first_repeated_char(s):
    char_set = set()
    for char in s:
        if char in char_set:
            return char
        char_set.add(char)
    return None
assert first_repeated_char("abcabc") == "a"
def first_repeated_char(s):
    char_set = set()
    for char in s:
        if char in char_set:
            return char
        char_set.add(char)
    return None

assert first_repeated_char("abcabc") == "a"
def first_repeated_char(s):
    char_set = set()
    for char in s:
        if char in char_set:
            return char
        char_set.add(char)
    return None

assert first_repeated_char("abcabc") == "a"
assert first_repeated_char("abcdef") == None
assert first_repeated_char("abca") == "a"
assert first_repeated_char("aabbcc") == "a"
assert first_repeated_char("") == None
assert first_repeated_char("abcabc") == "a"
assert first_repeated_char("abc") == None
assert first_repeated_char("123123") == "1"