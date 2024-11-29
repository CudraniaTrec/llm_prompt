def test_three_equal(a, b, c):
    equal_count = 0
    if a == b:
        equal_count += 1
    if b == c:
        equal_count += 1
    if a == c:
        equal_count += 1
    if equal_count == 3:
        return 3
    return equal_count
assert test_three_equal(1,1,1) == 3
assert test_three_equal(-1,-2,-3) == 0
assert test_three_equal(1,2,2) == 2