def sum_Of_product(n):
    from math import comb
    total_sum = 0
    for i in range(n):
        product = comb(n, i) * comb(n, i + 1)
        total_sum += product
    return total_sum
assert sum_Of_product(3) == 15
assert sum_Of_product(4) == 56
assert sum_Of_product(1) == 1