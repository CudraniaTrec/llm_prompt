def count_bidirectional(tuples_list):
    count = 0
    seen = set()
    for a, b in tuples_list:
        if (b, a) in seen:
            count += 1
        seen.add((a, b))
    return count
assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)] ) == 3
assert count_bidirectional([(5, 6), (1, 3), (6, 5), (9, 1), (6, 5), (2, 1)] ) == 2
assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 2), (6, 5), (2, 1)] ) == 4