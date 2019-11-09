class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        dp = [0] * n
        for i in range(n):
            if i < 2:
                dp[i] = cost[i]
            else:
                dp[i] = min(dp[i-1], dp[i-2]) + cost[i]

        return min(dp[i-1], dp[i-2])