
def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """

    def digit_sum(n):
        return sum(int(d) if n >= 0 else -int(d) for d in str(abs(n)))

    return sum(1 for num in arr if digit_sum(num) > 0)
def digit_sum(n):
    return sum(int(digit) if n >= 0 else -int(digit) for digit in str(abs(n)))

return sum(1 for num in arr if digit_sum(num) > 0)
    def digit_sum(n):
        return sum(int(digit) if n >= 0 else -int(digit) for digit in str(abs(n)))

    return sum(1 for num in arr if digit_sum(num) > 0)
    def digit_sum(n):
        return sum(int(d) if n >= 0 else -int(d) for d in str(abs(n)))

    return sum(1 for num in arr if digit_sum(num) > 0)
    def digit_sum(n):
        return sum(int(digit) if n >= 0 else -int(digit) for digit in str(abs(n)))

    return sum(1 for num in arr if digit_sum(num) > 0)
def check(candidate):

    # Check some simple cases
    assert candidate([]) == 0
    assert candidate([-1, -2, 0]) == 0
    assert candidate([1, 1, 2, -2, 3, 4, 5]) == 6
    assert candidate([1, 6, 9, -6, 0, 1, 5]) == 5
    assert candidate([1, 100, 98, -7, 1, -1]) == 4

    # Check some edge cases that are easy to work out by hand.


check(count_nums)