def common_element(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False
assert common_element([1,2,3,4,5], [5,6,7,8,9])==True
assert common_element([1,2,3,4,5], [6,7,8,9])==None
assert common_element(['a','b','c'], ['d','b','e'])==True