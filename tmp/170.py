def sum_range_list(lst, start_index, end_index):
    total_sum = sum(lst[start_index:end_index + 1])
    return total_sum
assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10) == 29
assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 5, 7) == 16
assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 7, 10) == 38