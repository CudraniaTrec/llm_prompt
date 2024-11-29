def max_of_nth(matrix, n):
    max_value = float('-inf')
    for row in matrix:
        if row[n] > max_value:
            max_value = row[n]
    return max_value
assert max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2) == 19
assert max_of_nth([[6, 7, 8], [2, 4, 6], [9, 10, 20]], 1) == 10
assert max_of_nth([[7, 8, 9], [3, 5, 7], [10, 11, 21]], 1) == 11