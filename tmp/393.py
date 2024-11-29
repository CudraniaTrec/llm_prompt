def max_length_list(lists):
    max_len = 0
    max_list = []
    for lst in lists:
        if len(lst) > max_len:
            max_len = len(lst)
            max_list = lst
    return (max_len, max_list)
def max_length_list(lists):
    max_len = 0
    max_list = []
    for lst in lists:
        if len(lst) > max_len:
            max_len = len(lst)
            max_list = lst
    return (max_len, max_list)

assert max_length_list([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])==(3, [13, 15, 17])
assert max_length_list([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])==(3, [13, 15, 17])
assert max_length_list([[1,2,3,4,5],[1,2,3,4],[1,2,3],[1,2],[1]])==(5,[1,2,3,4,5])
assert max_length_list([[3,4,5],[6,7,8,9],[10,11,12]])==(4,[6,7,8,9])