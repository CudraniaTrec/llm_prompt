def lcs_of_three(str1, str2, str3):
    m = len(str1)
    n = len(str2)
    o = len(str3)
    
    dp = [[[0] * (o + 1) for _ in range(n + 1)] for __ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            for k in range(1, o + 1):
                if str1[i - 1] == str2[j - 1] == str3[k - 1]:
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                else:
                    dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])
    
    return dp[m][n][o]

assert lcs_of_three('AGGT12', '12TXAYB', '12XBA') == 2
def lcs_of_three(str1, str2, str3):
    m = len(str1)
    n = len(str2)
    o = len(str3)
    
    dp = [[[0] * (o + 1) for _ in range(n + 1)] for __ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            for k in range(1, o + 1):
                if str1[i - 1] == str2[j - 1] == str3[k - 1]:
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                else:
                    dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])
    
    return dp[m][n][o]

assert lcs_of_three('AGGT12', '12TXAYB', '12XBA') == 2
assert lcs_of_three('AGGT12', '12TXAYB', '12XBA') == 2
assert lcs_of_three('Reels', 'Reelsfor', 'ReelsforReels') == 5
assert lcs_of_three('abcd1e2', 'bc12ea', 'bd1ea') == 3