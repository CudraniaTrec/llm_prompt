def sum_in_range(l, r):
    total_sum = 0
    for i in range(l, r + 1):
        if i % 2 != 0:
            total_sum += i
    return total_sum
assert sum_in_range(2,5) == 8
assert sum_in_range(5,7) == 12
assert sum_in_range(7,13) == 40