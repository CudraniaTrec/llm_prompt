def is_Diff(num):
    if num % 11 == 0:
        return True
    else:
        return False
assert is_Diff (12345) == False
assert is_Diff(1212112) == True
assert is_Diff(1212) == False