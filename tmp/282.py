def sub_list(list1, list2):
    return [a - b for a, b in zip(list1, list2)]
assert sub_list([1, 2, 3],[4,5,6])==[-3,-3,-3]
assert sub_list([1,2],[3,4])==[-2,-2]
assert sub_list([90,120],[50,70])==[40,50]