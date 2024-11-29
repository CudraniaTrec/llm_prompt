def first_odd(numbers):
    for number in numbers:
        if number % 2 != 0:
            return number
    return None
assert first_odd([1,3,5]) == 1
assert first_odd([2,4,1,3]) == 1
assert first_odd ([8,9,1]) == 9