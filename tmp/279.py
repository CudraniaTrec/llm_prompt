def is_num_decagonal(n):
    return n * (4 * n - 3)
assert is_num_decagonal(3) == 27
assert is_num_decagonal(7) == 175
assert is_num_decagonal(10) == 370