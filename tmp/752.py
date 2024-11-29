def jacobsthal_num(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return jacobsthal_num(n - 1) + 2 * jacobsthal_num(n - 2)

assert jacobsthal_num(5) == 11
assert jacobsthal_num(5) == 11
assert jacobsthal_num(2) == 1
assert jacobsthal_num(4) == 5
assert jacobsthal_num(13) == 2731