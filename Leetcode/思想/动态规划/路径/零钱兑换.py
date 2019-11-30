class Solution:
    def coinChange(self, coins, m):
        f = [float('inf')]*(m+1)
        f[0] = 0
        for i in range(1, m+1):
            for c in coins:
                if i - c >= 0:
                    f[i] = min(f[i], f[i-c]+1)
        return f[m] if f[m] != float('inf') else -1  # 如果为inf说明状态不可达，返回-1即可。