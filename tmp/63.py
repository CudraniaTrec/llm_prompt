def max_difference(tuple_list):
    max_diff = 0
    for a, b in tuple_list:
        difference = abs(a - b)
        if difference > max_diff:
            max_diff = difference
    return max_diff
assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7
assert max_difference([(4, 6), (2, 17), (9, 13), (11, 12)]) == 15
assert max_difference([(12, 35), (21, 27), (13, 23), (41, 22)]) == 23