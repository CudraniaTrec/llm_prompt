def check_integer(s):
    if s.isdigit() or (s.startswith('-') and s[1:].isdigit()):
        return True
    return False
assert check_integer("python")==False
assert check_integer("1")==True
assert check_integer("12345")==True