class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # n行m列
        # n是t，ｍ是s
        m, n = len(s) + 1, len(t) + 1
        dp = [[0] * m for _ in range(n)]
        for j in range(m):
            dp[0][j] = 1
        # 状态方程
        for i in range(1, n):
            for j in range(1, m):
                if t[i-1] == s[j-1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]

        return dp[n-1][m-1]


