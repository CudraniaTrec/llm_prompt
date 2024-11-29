def largest_neg(numbers):
    largest = None
    for num in numbers:
        if num < 0:
            if largest is None or num < largest:
                largest = num
    return largest
def largest_neg(numbers):
    largest = None
    for num in numbers:
        if num < 0:
            if largest is None or num < largest:
                largest = num
    return largest

assert largest_neg([1,2,3,-4,-6]) == -6
assert largest_neg([1,2,3,-4,-6]) == -6
assert largest_neg([1,2,3,-8,-9]) == -9
assert largest_neg([1,2,3,4,-1]) == -1