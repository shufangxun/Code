class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1] * (n + 1)
        # dp[0] = 1
        # dp[1] = 1
        # 从第二个开始状态转移
        for i in range(2, n+1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
