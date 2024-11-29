def extract_singly(nested_list):
    flat_set = set()
    for sublist in nested_list:
        flat_set.update(sublist)
    return flat_set
assert set(extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)])) == set([3, 4, 5, 7, 1])
assert set(extract_singly([(1, 2, 3), (4, 2, 3), (7, 8)])) == set([1, 2, 3, 4, 7, 8])
assert set(extract_singly([(7, 8, 9), (10, 11, 12), (10, 11)])) == set([7, 8, 9, 10, 11, 12])