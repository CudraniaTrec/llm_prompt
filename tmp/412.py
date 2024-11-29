def remove_odd(numbers):
    return [num for num in numbers if num % 2 == 0]
assert remove_odd([1,2,3]) == [2]
assert remove_odd([2,4,6]) == [2,4,6]
assert remove_odd([10,20,3]) == [10,20]