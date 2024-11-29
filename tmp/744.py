def check_none(tup):
    for item in tup:
        if item is None:
            return True
    return False
assert check_none((10, 4, 5, 6, None)) == True
assert check_none((7, 8, 9, 11, 14)) == False
assert check_none((1, 2, 3, 4, None)) == True