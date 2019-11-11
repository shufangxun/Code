# 动态规划 超时
def isSubsequence(s, t):
    m = len(s) + 1
    n = len(t) + 1
    dp = [[True] * n for _ in range(m)]

    for i in range(1, m):
        dp[i][0] = False

    for i in range(1, m):
        for j in range(1, n):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = dp[i][j-1]

    return dp[m-1][n-1]



# 双指针法
def isSubsequence1(s, t):
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            j += 1
    return False if i < len(s) else True