def difference(n):
    sum_of_cubes = sum(i**3 for i in range(1, n + 1))
    sum_of_natural_numbers = sum(i for i in range(1, n + 1))
    return sum_of_cubes - sum_of_natural_numbers
assert difference(3) == 30
assert difference(5) == 210
assert difference(2) == 6