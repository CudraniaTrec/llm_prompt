def total_match(lst1, lst2):
    total1 = sum(len(s) for s in lst1)
    total2 = sum(len(s) for s in lst2)
    
    if total1 < total2:
        return lst1
    else:
        return lst2
    total_chars_lst1 = sum(len(s) for s in lst1)
    total_chars_lst2 = sum(len(s) for s in lst2)
    
    if total_chars_lst1 < total_chars_lst2:
        return lst1
    else:
        return lst2
def check(candidate):

    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate([], []) == []
    assert candidate(['hi', 'admin'], ['hi', 'hi']) == ['hi', 'hi']
    assert candidate(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) == ['hi', 'admin']
    assert candidate(['4'], ['1', '2', '3', '4', '5']) == ['4']


    # Check some edge cases that are easy to work out by hand.


check(total_match)