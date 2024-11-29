def swap_List(lst):
    if len(lst) < 2:
        return lst
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst
assert swap_List([1,2,3]) == [3,2,1]
assert swap_List([1,2,3,4,4]) == [4,2,3,4,1]
assert swap_List([4,5,6]) == [6,5,4]