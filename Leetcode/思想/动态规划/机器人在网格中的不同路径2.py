class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        if not obstacleGrid:
            return 0
        n = len(obstacleGrid[0])
        m = len(obstacleGrid)
        dp = [[0] * n for _ in range(m)]
        # 统一起来：不阻碍时为1；阻碍时为0
        dp[0][0] = 1 - obstacleGrid[0][0]
        for j in range(1, m):
            dp[j][0] = dp[j - 1][0] * (1 - obstacleGrid[j][0])
        for i in range(1, n):
            dp[0][i] = dp[0][i - 1] * (1 - obstacleGrid[0][i])
        # 状态方程
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = (dp[i][j - 1]+dp[i - 1][j]) * (1 - obstacleGrid[i][j])
        return dp[-1][-1]