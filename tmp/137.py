import math
def zero_count(arr):
    zeroes = sum(1 for x in arr if x == 0)
    non_zeroes = sum(1 for x in arr if x != 0)
    if non_zeroes == 0:
        return float('inf')
    return zeroes / non_zeroes
import math
def zero_count(arr):
    zeroes = sum(1 for x in arr if x == 0)
    non_zeroes = sum(1 for x in arr if x != 0)
    if non_zeroes == 0:
        return float('inf')
    return zeroes / non_zeroes
assert math.isclose(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.181818, rel_tol=0.001)
import math
def zero_count(arr):
    zeroes = sum(1 for x in arr if x == 0)
    non_zeroes = sum(1 for x in arr if x != 0)
    if non_zeroes == 0:
        return float('inf')
    return zeroes / non_zeroes
assert math.isclose(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.181818, rel_tol=0.001)
assert math.isclose(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.181818, rel_tol=0.001)
assert math.isclose(zero_count([2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8]), 0.00, rel_tol=0.001)
assert math.isclose(zero_count([2, 4, -6, -9, 11, -12, 14, -5, 17]), 0.00, rel_tol=0.001)