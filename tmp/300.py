import math
import math

def count_binary_seq(n):
    if n == 0:
        return 1.0
    return math.comb(2 * n, n) / (n + 1)
assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(2), 6.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(3), 20.0, rel_tol=0.001)