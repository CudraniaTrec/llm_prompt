def closest_num(n):
    if n <= 0:
        return None
    return n - 1
assert closest_num(11) == 10
assert closest_num(7) == 6
assert closest_num(12) == 11