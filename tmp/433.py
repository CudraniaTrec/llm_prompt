def check_greater(arr, num):
    for element in arr:
        if num <= element:
            return False
    return True
assert check_greater([1, 2, 3, 4, 5], 4) == False
assert check_greater([2, 3, 4, 5, 6], 8) == True
assert check_greater([9, 7, 4, 8, 6, 1], 11) == True