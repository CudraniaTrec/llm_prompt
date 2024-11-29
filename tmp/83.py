def get_Char(s):
    total_ascii = sum(ord(char) for char in s)
    char_index = total_ascii % 26
    return chr(char_index + ord('a'))
assert get_Char("abc") == "f"
assert get_Char("gfg") == "t"
assert get_Char("ab") == "c"