import math
def harmonic_sum(n):
    total = 0.0
    for i in range(1, n):
        total += 1 / i
    return total
assert math.isclose(harmonic_sum(7), 2.5928571428571425, rel_tol=0.001)
assert math.isclose(harmonic_sum(4), 2.083333333333333, rel_tol=0.001)
assert math.isclose(harmonic_sum(19), 3.547739657143682, rel_tol=0.001)