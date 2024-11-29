def _sum(arr):
    total = 0
    for num in arr:
        total += num
    return total
assert _sum([1, 2, 3]) == 6
assert _sum([15, 12, 13, 10]) == 50
assert _sum([0, 1, 2]) == 3