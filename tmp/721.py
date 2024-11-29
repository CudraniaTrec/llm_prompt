def maxAverageOfPath(matrix):
    from collections import deque
    
    n = len(matrix)
    dp = [[0] * n for _ in range(n)]
    count = [[0] * n for _ in range(n)]
    
    dp[0][0] = matrix[0][0]
    count[0][0] = 1
    
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            if i > 0:
                if dp[i][j] < dp[i - 1][j] + matrix[i][j]:
                    dp[i][j] = dp[i - 1][j] + matrix[i][j]
                    count[i][j] = count[i - 1][j] + 1
            if j > 0:
                if dp[i][j] < dp[i][j - 1] + matrix[i][j]:
                    dp[i][j] = dp[i][j - 1] + matrix[i][j]
                    count[i][j] = count[i][j - 1] + 1
    
    return dp[n - 1][n - 1] / count[n - 1][n - 1]
assert maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]) == 5.2
assert maxAverageOfPath([[2, 3, 4], [7, 6, 5], [8, 4, 10]]) == 6.2
assert maxAverageOfPath([[3, 4, 5], [8, 7, 6], [9, 5, 11]]) == 7.2
assert maxAverageOfPath([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 5.8