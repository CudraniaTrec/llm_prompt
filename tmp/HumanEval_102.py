
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """

    if x > y:
        return -1
        
    max_even = y if y % 2 == 0 else y - 1
    
    if max_even < x:
        return -1
    
    return max_even
    if x > y:
        x, y = y, x
    
    max_even = y if y % 2 == 0 else y - 1
    if max_even < x:
        return -1

    return max_even
    if x > y:
        return -1
    max_even = y if y % 2 == 0 else y - 1
    if max_even < x:
        return -1
    return max_even
def check(candidate):

    # Check some simple cases
    assert candidate(12, 15) == 14
    assert candidate(13, 12) == -1
    assert candidate(33, 12354) == 12354
    assert candidate(5234, 5233) == -1
    assert candidate(6, 29) == 28

    # Check some edge cases that are easy to work out by hand.


check(choose_num)