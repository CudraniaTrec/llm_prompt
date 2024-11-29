def two_unique_nums(lst):
    unique = []
    for num in lst:
        if lst.count(num) == 1:
            unique.append(num)
    return unique
assert two_unique_nums([1,2,3,2,3,4,5]) == [1, 4, 5]
assert two_unique_nums([1,2,3,2,4,5]) == [1, 3, 4, 5]
assert two_unique_nums([1,2,3,4,5]) == [1, 2, 3, 4, 5]