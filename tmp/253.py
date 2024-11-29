def count_integer(lst):
    count = 0
    for element in lst:
        if isinstance(element, int):
            count += 1
    return count
assert count_integer([1,2,'abc',1.2]) == 2
assert count_integer([1,2,3]) == 3
assert count_integer([1,1.2,4,5.1]) == 2