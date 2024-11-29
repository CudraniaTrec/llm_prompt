def exchange(lst1, lst2):
    even_count = sum(1 for x in lst1 if x % 2 == 0)
    odd_count = len(lst1) - even_count
    
    if odd_count <= sum(1 for x in lst2 if x % 2 == 0):
        return "YES"
    return "NO"
    even_count = sum(1 for x in lst1 if x % 2 == 0)
    odd_count = len(lst1) - even_count
    if odd_count <= sum(1 for x in lst2 if x % 2 == 0):
        return "YES"
    return "NO"
    even_count = sum(1 for x in lst1 if x % 2 == 0)
    odd_count = len(lst1) - even_count
    if odd_count <= sum(1 for x in lst2 if x % 2 == 0):
        return "YES"
    else:
        return "NO"
    even_count = sum(1 for x in lst1 if x % 2 == 0)
    odd_count = len(lst1) - even_count
    if odd_count <= sum(1 for x in lst2 if x % 2 == 0):
        return "YES"
    return "NO"
    even_count = sum(1 for x in lst1 if x % 2 == 0)
    odd_count = len(lst1) - even_count
    if odd_count <= sum(1 for x in lst2 if x % 2 == 0):
        return "YES"
    else:
        return "NO"
    even_count = sum(1 for x in lst1 if x % 2 == 0)
    odd_count = len(lst1) - even_count
    if odd_count <= sum(1 for x in lst2 if x % 2 == 0):
        return "YES"
    else:
        return "NO"
def check(candidate):

    # Check some simple cases
    assert candidate([1, 2, 3, 4], [1, 2, 3, 4]) == "YES"
    assert candidate([1, 2, 3, 4], [1, 5, 3, 4]) == "NO"
    assert candidate([1, 2, 3, 4], [2, 1, 4, 3]) == "YES" 
    assert candidate([5, 7, 3], [2, 6, 4]) == "YES"
    assert candidate([5, 7, 3], [2, 6, 3]) == "NO" 

    # Check some edge cases that are easy to work out by hand.


check(exchange)