class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0 for _ in range(len(coins) + 1)] for _ in range(amount + 1)]
        for j in range(len(coins) + 1):
            dp[0][j] = 1

        for i in range(amount + 1):
            for j in range(1, len(coins) + 1):
                if i >= coins[j - 1]:
                    dp[i][j] = dp[i - coins[j - 1]][j] + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]
        return dp[-1][-1]


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
        	for i in range(1, amount + 1):
        		if i >= coin:
        			dp[i] = dp[i] + dp[i - coin]

        return dp[-1] 