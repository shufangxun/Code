# 动态规划

## 戳气球

> 1、有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。  
> 2、要求戳破所有的气球。每当你戳破一个气球 i 时，你可以获得 nums[left] * nums[i] * nums[right] 个硬币。 这里的 left 和 right 代表和 i 相邻的两个气球的序号。  
> 2、当戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。
> 3、求所能获得硬币的最大数量。

解法： 动态规划

1. 状态
设$dp[i][j]$为$i$到$j$的序列最大值，所以要求的是dp[0][n-1]
2. 状态转移方程
如何转移$dp[i][j]$，可以从最后一个出的气球作为突破口：  
   1. 在出最后一个之前，左右两边都是计算好，不受影响的
   2. 所以设$k$为最后一个出的元素，其对应值为$nums[i-1] * nums[k] * nums[j+1]$
   3. 前面两个$dp[i][k-1]$和$dp[k+1][j]$不受影响
   4. $dp[i][j] = max(dp[i][j], nums[i-1] * nums[k] * nums[j+1] + dp[i])[k-1] + dp[k+1][j])$
3. 边界条件  
k在最左边或者最右边时：$nums[-1] * nums[i] * nums[n]$，$nums[-1] = 1$，$nums[n] = 1$

4. 实现
实现上有点差异
   1. 前后补充两个哨兵元素[1]，然后$dp[i][j]$： 表示$i,j$不戳破，中间产生的最大价值，其中$k$是最后戳破的，$i < k < j$
   2. 因此输出时$dp[0][n-1]$
   3. $i ~ j$之间至少有一个元素， $j - i == 2$

```python
def maxCoins(nums):
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for gap in range(2, n): # 遍历gap范围
            for i in range(0, n-gap):
                j = i + gap
                for k in range(i+1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j])
        return dp[0][n-1]
```
