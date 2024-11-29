

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """

    if not l:
        return True
    
    increasing = None
    
    for i in range(1, len(l)):
        if l[i] > l[i - 1]:
            if increasing is None:
                increasing = True
            elif not increasing:
                return False
        elif l[i] < l[i - 1]:
            if increasing is None:
                increasing = False
            elif increasing:
                return False
    
    return True


METADATA = {}


def check(candidate):
    assert candidate([1, 2, 4, 10]) == True
    assert candidate([1, 2, 4, 20]) == True
    assert candidate([1, 20, 4, 10]) == False
    assert candidate([4, 1, 0, -10]) == True
    assert candidate([4, 1, 1, 0]) == True


check(monotonic)