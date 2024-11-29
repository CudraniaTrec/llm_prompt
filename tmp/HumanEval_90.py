def next_smallest(lst):
    if len(lst) < 2:
        return None
    unique_lst = list(set(lst))
    unique_lst.sort()
    return unique_lst[1] if len(unique_lst) > 1 else None
def check(candidate):

    # Check some simple cases
    assert candidate([1, 2, 3, 4, 5]) == 2
    assert candidate([5, 1, 4, 3, 2]) == 2
    assert candidate([]) == None
    assert candidate([1, 1]) == None
    assert candidate([1,1,1,1,0]) == 1

    # Check some edge cases that are easy to work out by hand.


check(next_smallest)