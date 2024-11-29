
def prod_signs(arr):
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> prod_signs([1, 2, 2, -4]) == -9
    >>> prod_signs([0, 1]) == 0
    >>> prod_signs([]) == None
    """

    if not arr:
        return None
    
    magnitude_sum = sum(abs(x) for x in arr)
    product_sign = 1
    
    for num in arr:
        if num > 0:
            product_sign *= 1
        elif num < 0:
            product_sign *= -1
        else:
            product_sign = 0
            break
    
    return magnitude_sum * product_sign
def check(candidate):

    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate([1, 2, 2, -4]) == -9
    assert candidate([0, 1]) == 0
    assert candidate([1, 1, 1, 2, 3, -1, 1]) == -10
    assert candidate([]) == None

    # Check some edge cases that are easy to work out by hand.


check(prod_signs)