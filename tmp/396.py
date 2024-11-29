def check_char(s):
    if s[0] == s[-1]:
        return "Valid"
    else:
        return "Invalid"
assert check_char("abba") == "Valid"
assert check_char("a") == "Valid"
assert check_char("abcd") == "Invalid"