def Diff(list1, list2):
    return [item for item in list1 if item not in list2] + [item for item in list2 if item not in list1]
def Diff(list1, list2):
    combined_diff = [item for item in list1 if item not in list2] + [item for item in list2 if item not in list1]
    return combined_diff
def Diff(list1, list2):
    combined_diff = list(set(list1) ^ set(list2))
    return combined_diff
def Diff(list1, list2):
    combined_diff = list(set(list1) ^ set(list2))
    return sorted(combined_diff, key=lambda x: (list1 + list2).index(x))
def Diff(list1, list2):
    combined_diff = list(set(list1) ^ set(list2))
    return sorted(combined_diff, key=lambda x: (list1 + list2).index(x))
assert (Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) == [10, 20, 30, 15]
assert (Diff([1,2,3,4,5], [6,7,1])) == [2,3,4,5,6,7]
assert (Diff([1,2,3], [6,7,1])) == [2,3,6,7]