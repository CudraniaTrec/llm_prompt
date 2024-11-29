def min_val(lst):
    min_value = float('inf')
    for item in lst:
        if isinstance(item, (int, float)) and item < min_value:
            min_value = item
    return min_value if min_value != float('inf') else None
assert min_val(['Python', 3, 2, 4, 5, 'version'])==2
assert min_val(['Python', 15, 20, 25])==15
assert min_val(['Python', 30, 20, 40, 50, 'version'])==20