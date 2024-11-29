def next_Perfect_Square(n):
    import math
    next_square_root = math.ceil(math.sqrt(n)) + 1
    return next_square_root ** 2
assert next_Perfect_Square(35) == 36
assert next_Perfect_Square(6) == 9
assert next_Perfect_Square(9) == 16