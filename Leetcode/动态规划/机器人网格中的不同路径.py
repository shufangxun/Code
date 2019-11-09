class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # 边界条件 当时边界时只有只有一种方向 = 1
        dp = [[1] * n for _ in range(m)]

        # 状态方程
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j-1]+dp[i-1][j]
        return dp[-1][-1]