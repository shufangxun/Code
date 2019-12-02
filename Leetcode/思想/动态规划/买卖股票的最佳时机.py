# 买卖股票的最佳时机
## 法1
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        dp = [0] * len(prices)
        minPrice = prices[0]
        for i in range(1, len(prices)):
            dp[i] = max(dp[i - 1], prices[i] - minPrice)
            minPrice = min(minPrice, prices[i])
        return max(dp)

## 法2
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<=1:
            return 0
        diff = [0 for _ in range(len(prices)-1)]
        for i in range(len(prices)-1):
            diff[i] = prices[i+1]-prices[i]
        dp = [0 for _ in range(len(prices)-1)]
        dp[0] = max(0, diff[0])
        max_profit = dp[0]
        for i in range(1, len(prices)-1):
            dp[i] = max(0, diff[i]+dp[i-1])
            max_profit = max(max_profit, dp[i])
        return max_profit

