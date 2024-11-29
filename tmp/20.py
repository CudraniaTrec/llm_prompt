def is_woodall(n):
    if n < 0:
        return False
    woodall_numbers = []
    for k in range(n + 1):
        woodall_number = (2 ** k) - k
        if woodall_number > n:
            break
        woodall_numbers.append(woodall_number)
    return n in woodall_numbers
assert is_woodall(383) == True
assert is_woodall(254) == False
assert is_woodall(200) == False