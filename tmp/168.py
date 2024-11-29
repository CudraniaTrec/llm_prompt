def frequency(lst, num):
    count = 0
    for element in lst:
        if element == num:
            count += 1
    return count
assert frequency([1,2,3], 4) == 0
assert frequency([1,2,2,3,3,3,4], 3) == 3
assert frequency([0,1,2,3,1,2], 1) == 2