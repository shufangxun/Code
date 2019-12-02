# 动态规划

## 戳气球

> 1、有 $n$ 个气球，编号为 $0$ 到 $n-1$，每个气球上都标有一个数字，这些数字存在数组 $nums$ 中  
> 2、要求戳破所有的气球。每当你戳破一个气球 i 时，你可以获得 $nums[left] * nums[i] * nums[right]$ 个硬币。 这里的 left 和 right 代表和 i 相邻的两个气球的序号。  
> 3、当戳破了气球 $i$ 后，气球 $left$ 和气球 $right$ 就变成了相邻的气球。  
> 4、求所能获得硬币的最大数量。

思路

1. 状态
设 $dp[i][j]$ 为 $i$ 到 $j$ 的序列最大值，所以要求的是 $dp[0][n-1]$
2. 状态转移方程
如何转移$dp[i][j]$，可以从最后一个出的气球作为突破口：
   1. 在出最后一个之前，左右两边都是计算好，不受影响的
   2. 所以设$k$为最后一个出的元素，其对应值为$nums[i-1] * nums[k] * nums[j+1]$
   3. 前面两个$dp[i][k-1]$和$dp[k+1][j]$不受影响
   4. $dp[i][j] = max(dp[i][j], nums[i-1] * nums[k] * nums[j+1] + dp[i])[k-1] + dp[k+1][j])$
3. 边界条件  
k在最左边或者最右边时：$nums[-1] * nums[i] * nums[n]$，$nums[-1] = 1$，$nums[n] = 1$
4. 实现 实现上有点差异  
   1. 前后补充两个哨兵元素 [1]，然后 $dp[i][j]$： 表示 $i,j$ 不戳破，中间产生的最大价值，其中$k$是最后戳破的，$i < k < j$
   2. 因此输出是 $dp[0][n-1]$
   3. $i ~ j$ 之间至少有一个元素， $j - i == 2$

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

## 最大正方形

> 在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积

- 状态  
$dp[i][j]$ 是以其为右下角的正方形最大边
- 状态方程  
  $dp[i][j]$ 是左边$dp[i-1][j]$，上边$dp[i][j-1]$和斜上$dp[i-1][j-1]$的最大边 $+1$
- 边界方程  
  1. 当为空时，返回０
  2. 当$matrix[i][j]=0$，$dp[i][j]=0$
  3. 当为第一行和第一列时，$dp[i][j]=matrix[i][j]-0
- 时间复杂度；$O(mn)$  
- 空间复杂度：$O(mn)$

```python
def maximalSquare(matrix):
   if not matrix: return 0
   m, n = len(matrix), len(matrix[0]) # m为行数 n为列数
   dp = [[0] * n for _ in range(m)]
   size = 0 # 边长
   for i in range(0, m):
      for j in range(0, n):
            if matrix[i][j] == '0' or i == 0 or j == 0:
               dp[i][j] = int(matrix[i][j]) - 0
            else:
               dp[i][j] = int(min(dp[i - 1][j - 1], min(dp[i - 1][j], dp[i][j - 1]))) + 1
            size = max(dp[i][j], size)
   return size * size
```

- 优化
- 时间复杂度: $O(mn)$
- 空间复杂度: $O(n)$

```python
def maximalSquare(self, matrix):
   if not matrix: return 0
   m, n = len(matrix), len(matrix[0]) # m为行数 n为列数
   dp = [0] * n
   size = 0 # 边长
   pre = 0
   for i in range(0, m):
      for j in range(0, n):
            tmp = dp[j]
            if matrix[i][j] == '0' or i == 0 or j == 0:
               dp[j] = int(matrix[i][j]) - 0
            else:
               dp[j] = int(min(dp[j], dp[j - 1], pre)) + 1 # 优化 O(n)
            size = max(dp[j], size)
   return size * size
```

## 最大矩形

> 给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积

思路；结合柱状图中最大矩形的面积的方法，统计每一行上每一列的 1 的高度

```python
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) <= 0: return 0
        heights = [0] * len(matrix[0])
        maxArea = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == '1':
                    heights[col] += 1
                else:
                    heights[col] = 0
            maxArea = max(maxArea, self.largestRectangleArea(heights))
        return maxArea
```

## 买卖股票的最佳时机系列

### I

> 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格，求最大利润

法1：前i天的最大收益 = max{前i-1天的最大收益，第i天的价格-前i-1天中的最小价格}

```python
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
```

法2：区间和跟求差可以相互转换。题目就转变为求最大连续子数组和

- 首先构造 diff 数组，求连续两天的价格差
- 状态转移方程 dp[i] = max(dp[i-1] + diff[i], 0), dp[i] 指以 i 元素结尾的子数组的最大和
- 接着遍历 diff 数组，根据状态转移方程求出 dp 数组
- 最后 dp 数组中的最大值就是最大价格差

```python
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
```

