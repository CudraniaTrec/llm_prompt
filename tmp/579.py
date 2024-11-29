def find_dissimilar(tuple1, tuple2):
    unique_elements = set(tuple1).symmetric_difference(set(tuple2))
    return tuple(unique_elements)
assert find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)) == (3, 6, 7, 10)
assert find_dissimilar((1, 2, 3, 4), (7, 2, 3, 9)) == (1, 4, 7, 9)
assert find_dissimilar((21, 11, 25, 26), (26, 34, 21, 36)) == (34, 36, 11, 25)