def Find_Min_Length(lists):
    if not lists:
        return 0
    min_length = len(lists[0])
    for lst in lists:
        min_length = min(min_length, len(lst))
    return min_length
def Find_Min_Length(lists):
    if not lists:
        return 0
    min_length = len(lists[0])
    for lst in lists:
        min_length = min(min_length, len(lst))
    return min_length

assert Find_Min_Length([[1],[1,2]]) == 1
assert Find_Min_Length([[1],[1,2]]) == 1
assert Find_Min_Length([[1,2],[1,2,3],[1,2,3,4]]) == 2
assert Find_Min_Length([[3,3,3],[4,4,4,4]]) == 3