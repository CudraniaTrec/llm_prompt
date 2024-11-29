
def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    """

    return sorted(arr, key=lambda x: (bin(x).count('1'), x))
    return sorted(arr, key=lambda x: (bin(x).count('1'), x))
    return sorted(arr, key=lambda x: (bin(x).count('1'), x))
    return sorted(arr, key=lambda x: (bin(x).count('1'), x))
    return sorted(arr, key=lambda x: (bin(x).count('1'), x))
    return sorted(arr, key=lambda x: (bin(x).count('1'), x))
    return sorted(arr, key=lambda x: (bin(x).count('1'), x))
    return sorted(arr, key=lambda x: (bin(x).count('1'), x))
    return sorted(arr, key=lambda x: (bin(x).count('1'), x))
    return sorted(arr, key=lambda x: (bin(x).count('1'), x))
    return sorted(arr, key=lambda x: (bin(x).count('1'), x))
    return sorted(arr, key=lambda x: (bin(x).count('1'), x))
    return sorted(arr, key=lambda x: (bin(x).count('1'), x))
    return sorted(arr, key=lambda x: (bin(x).count('1'), x))
    return sorted(arr, key=lambda x: (bin(x).count('1'), x))
    return sorted(arr, key=lambda x: (bin(x).count('1'), x))
    return sorted(arr, key=lambda x: (bin(x).count('1'), x))
def check(candidate):

    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate([1,5,2,3,4]) == [1, 2, 4, 3, 5]
    assert candidate([-2,-3,-4,-5,-6]) == [-4, -2, -6, -5, -3]
    assert candidate([1,0,2,3,4]) == [0, 1, 2, 4, 3]
    assert candidate([]) == []

    # Check some edge cases that are easy to work out by hand.


check(sort_array)