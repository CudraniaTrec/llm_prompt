def is_perfect_square(n):
    if n < 0:
        return False
    x = int(n**0.5)
    return x * x == n
assert not is_perfect_square(10)
assert is_perfect_square(36)
assert not is_perfect_square(14)
assert is_perfect_square(14*14)
assert not is_perfect_square(125)