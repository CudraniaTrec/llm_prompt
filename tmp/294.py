def max_val(lst):
    maximum = float('-inf')
    for item in lst:
        if isinstance(item, (int, float)):
            if item > maximum:
                maximum = item
    return maximum
assert max_val(['Python', 3, 2, 4, 5, 'version'])==5
assert max_val(['Python', 15, 20, 25])==25
assert max_val(['Python', 30, 20, 40, 50, 'version'])==50