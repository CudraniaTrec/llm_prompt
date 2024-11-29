def get_total_number_of_sequences(m, n):
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        dp[i][1] = 1
    for length in range(2, n + 1):
        for last in range(1, m + 1):
            start = last // 2 + 1
            end = min(m, last)
            if start <= end:
                dp[last][length] = sum(dp[i][length - 1] for i in range(start, end + 1))
    return sum(dp[i][n] for i in range(1, m + 1))
assert get_total_number_of_sequences(10, 4) == 4
assert get_total_number_of_sequences(5, 2) == 6
assert get_total_number_of_sequences(16, 3) == 84