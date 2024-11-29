def first_non_repeating_character(s):
    char_count = {}
    
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            
    for char in s:
        if char_count[char] == 1:
            return char
            
    return None
def first_non_repeating_character(s):
    char_count = {}
    
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            
    for char in s:
        if char_count[char] == 1:
            return char
            
    return None

assert first_non_repeating_character("abcabc") == None
assert first_non_repeating_character("abcabc") == None
assert first_non_repeating_character("abc") == "a"
assert first_non_repeating_character("ababc") == "c"