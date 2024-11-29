def smallest_num(lst):
    if not lst:
        return None
    smallest = lst[0]
    for num in lst:
        if num < smallest:
            smallest = num
    return smallest
assert smallest_num([10, 20, 1, 45, 99]) == 1
assert smallest_num([1, 2, 3]) == 1
assert smallest_num([45, 46, 50, 60]) == 45