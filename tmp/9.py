def find_Rotations(s):
    if not s:
        return 0
    n = len(s)
    ss = s + s
    for i in range(1, n + 1):
        if ss[i:i+n] == s:
            return i
    return n
def find_Rotations(s):
    if not s:
        return 0
    n = len(s)
    ss = s + s
    for i in range(1, n + 1):
        if ss[i:i+n] == s:
            return i
    return n
assert find_Rotations("aaaa") == 1
assert find_Rotations("aaaa") == 1
assert find_Rotations("ab") == 2
assert find_Rotations("abc") == 3