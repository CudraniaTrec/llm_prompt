def tuple_str_int(s):
    return tuple(map(int, s.strip('()').split(',')))
assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
assert tuple_str_int("(1, 2, 3)") == (1, 2, 3)
assert tuple_str_int("(4, 5, 6)") == (4, 5, 6)
assert tuple_str_int("(7, 81, 19)") == (7, 81, 19)