from collections import Counter

def search(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    '''
    count = Counter(lst)
    result = -1
    for num in sorted(count.keys(), reverse=True):
        if count[num] >= num:
            result = num
            break
    return result
    count = Counter(lst)
    result = -1
    for num in sorted(count.keys(), reverse=True):
        if count[num] >= num:
            result = num
            break
    return result
    count = Counter(lst)
    result = -1
    for num in sorted(count.keys(), reverse=True):
        if count[num] >= num:
            result = num
            break
    return result
def check(candidate):

    # manually generated tests
    assert candidate([5, 5, 5, 5, 1]) == 1
    assert candidate([4, 1, 4, 1, 4, 4]) == 4
    assert candidate([3, 3]) == -1
    assert candidate([8, 8, 8, 8, 8, 8, 8, 8]) == 8
    assert candidate([2, 3, 3, 2, 2]) == 2

    # automatically generated tests


check(search)