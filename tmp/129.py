def magic_square_test(matrix):
    n = len(matrix)
    expected_sum = n * (n**2 + 1) // 2
    
    # Check rows
    for row in matrix:
        if sum(row) != expected_sum:
            return False
    
    # Check columns
    for col in range(n):
        if sum(matrix[row][col] for row in range(n)) != expected_sum:
            return False
    
    # Check diagonals
    if sum(matrix[i][i] for i in range(n)) != expected_sum:
        return False
    if sum(matrix[i][n - 1 - i] for i in range(n)) != expected_sum:
        return False
    
    return True
assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 8]])==True
assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 7]])==False