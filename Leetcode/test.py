def coinChange1(coins, m):
        f = [float('inf')]*(m+1)
        f[0] = 0
        for i in range(1, m+1):
            for c in coins:
                if i - c >= 0:
                    f[i] = min(f[i], f[i-c]+1)
        return f[m] if f[m] != float('inf') else -1  # 如果为inf说明状态不可达，返回-1即可。

def coinChange2(coins, m):
    f = [float('inf')] * (m + 1)
    f[0] = 0
    for c in coins:  # 枚举硬币总数
        for j in range(m, c-1, -1):  # 从大到小枚举金额，确保j-c >= 0.
            f[j] = min(f[j], f[j - c] + 1)
    return f[m] if f[m] != float('inf') else -1  # 如果为inf说明状态不可达，返回-1即可。

coins = list([1,2,4,5,10])
total1 = 20
total2 = 11
print(coinChange1(coins, total1))
print(coinChange2(coins, total2))
