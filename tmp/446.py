def count_Occurrence(tup, lst):
    count = 0
    for item in lst:
        count += tup.count(item)
    return count
def count_Occurrence(tup, lst):
    count = 0
    for item in lst:
        count += tup.count(item)
    return count
def count_Occurrence(tup, lst):
    count = 0
    for item in lst:
        count += tup.count(item)
    return count
assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b'] ) == 3
assert count_Occurrence((1, 2, 3, 1, 4, 6, 7, 1, 4),[1, 4, 7]) == 6
assert count_Occurrence((1,2,3,4,5,6),[1,2]) == 2