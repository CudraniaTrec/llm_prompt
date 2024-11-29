def eulerian_num(n, m):
    A = [[0] * (n + 1) for _ in range(n + 1)]
    A[0][0] = 1
    
    for i in range(1, n + 1):
        for j in range(i + 1):
            A[i][j] = (i - j) * A[i - 1][j] + (j + 1) * A[i - 1][j - 1]
    
    return A[n][m]
def eulerian_num(n, m):
    A = [[0] * (n + 1) for _ in range(n + 1)]
    A[0][0] = 1
    
    for i in range(1, n + 1):
        for j in range(i + 1):
            if j == 0:
                A[i][j] = (i - j) * A[i - 1][j]
            else:
                A[i][j] = (i - j) * A[i - 1][j] + (j + 1) * A[i - 1][j - 1]
    
    return A[n][m]
assert eulerian_num(3, 1) == 4
assert eulerian_num(4, 1) == 11
assert eulerian_num(5, 3) == 26