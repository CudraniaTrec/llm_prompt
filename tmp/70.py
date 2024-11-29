def get_equal(tuples_list):
    if not tuples_list:
        return True
    first_length = len(tuples_list[0])
    for tup in tuples_list:
        if len(tup) != first_length:
            return False
    return True
def get_equal(tuples_list):
    if not tuples_list:
        return True
    first_length = len(tuples_list[0])
    for tup in tuples_list:
        if len(tup) != first_length:
            return False
    return True
assert get_equal([(11, 22, 33), (44, 55, 66)]) == True
assert get_equal([(1, 2, 3), (4, 5, 6, 7)]) == False
assert get_equal([(1, 2), (3, 4)]) == True