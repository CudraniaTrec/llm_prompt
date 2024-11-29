def extract_freq(tuples_list):
    unique_tuples = set(tuples_list)
    return len(unique_tuples)
def extract_freq(tuples_list):
    unique_tuples = set()
    for tuple in tuples_list:
        unique_tuples.add(tuple)
    return len(unique_tuples)
def extract_freq(tuples_list):
    unique_tuples = set()
    for tuple in tuples_list:
        unique_tuples.add(tuple)
    return len(unique_tuples)
def extract_freq(tuples_list):
    unique_tuples = set()
    for tuple in tuples_list:
        unique_tuples.add(tuple)
    return len(unique_tuples)
def extract_freq(tuples_list):
    unique_tuples = set()
    for item in tuples_list:
        unique_tuples.add(tuple(sorted(item)))
    return len(unique_tuples)
assert extract_freq([(3, 4), (1, 2), (4, 3), (5, 6)] ) == 3
assert extract_freq([(4, 15), (2, 3), (5, 4), (6, 7)] ) == 4
assert extract_freq([(5, 16), (2, 3), (6, 5), (6, 9)] ) == 4