# 动态规划

## 戳气球

> 1、有 $n$ 个气球，编号为 $0$ 到 $n-1$，每个气球上都标有一个数字，这些数字存在数组 $nums$ 中  
> 2、要求戳破所有的气球。每当你戳破一个气球 i 时，你可以获得 $nums[left] * nums[i] * nums[right]$ 个硬币。 这里的 left 和 right 代表和 i 相邻的两个气球的序号。  
> 3、当戳破了气球 $i$ 后，气球 $left$ 和气球 $right$ 就变成了相邻的气球。  
> 4、求所能获得硬币的最大数量。

解法： 动态规划

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

## 连续子数组最大和

> 给定一个整数数组 $nums$ ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和

解法：除了状态转移，还要看怎么遍历

```python
def sumofsubS(nums):
   cursum = 0 #当前和
   ans = nums[0] # 最后结果
   for i in range(n):
      if cursum > 0:
         cursum += nums[i]
      else:
         cursum = nums[i]
      ans = max(cursum, ans)
   return ans
```

## 爬楼梯方式

> 需要 $n$ 阶才能到达楼顶，每次可以爬 $1$ 或 $2$ 个台阶。请问有多少种不同的方法可以爬到楼顶

解法:

- 状态  
$dp[i]$：$i$ 个台阶爬楼梯的方法
- 状态方程
爬 $i$ 个台阶的总方法数是前面一步爬 $1$ 个台阶和爬 $2$ 个台阶的总和
$dp[i] = dp[i - 1] + dp[i - 2]$
- 遍历  
从第一个台阶开始遍历

```python
def climbStairs(n):
   dp = [1] * (n + 1)
   # dp[0] = 1
   # dp[1] = 1
   # 从第二个开始状态转移
   for i in range(2, n+1):
      dp[i] = dp[i - 1] + dp[i - 2]
   return dp[n]
```

## 爬楼梯的最小消费

>1 . 数组的每个索引做为一个阶梯，第 $i$ 个阶梯对应着一个非负数的体力花费值 $cost[i]$ (索引从 $0$ 开始)  
>2 . 每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯  
>3 . 在开始时，你可以选择从索引为 $0$ 或 $1$ 的元素作为初始阶梯

解法：

- 状态  
$dp[i]$：爬到第 $i$ 个台阶需要的体力
- 转移方程  
爬到当前台阶花费的体力，是 $min(爬两次，爬一次)$ + 当前 $cost[i]$
- 边界条件
   1. $dp[0]$和$dp[1]$不能执行这个转移方程，等于对应的$cost$
   2. 如果距离终点有一级，直接爬两级出楼梯，最小 $cost$ 在 $dp[n-2]$；或者爬一级之后再出，最小 $cost$ 在 $dp[n-1]$

```python
def minCostClimbingStairs(cost):
   n = len(cost)
   dp = [0] * n
   for i in range(n):
      if i < 2:
            dp[i] = cost[i]
      else:
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]

   return min(dp[i-1], dp[i-2])
```

## 机器人在网格中的不同路径

> 1 . 一个机器人位于一个 $m \cdot n$ 网格的左上角，机器人每次只能向下或者向右移动一步，机器人试图达到网格的右下角  
> 2 . 求从左上角到右下角的不同路径

- 状态方程  
$dp[i][j] = dp[i][j-1]+dp[i-1][j]$
- 边界条件  
在边界时，只有一种方向可以走，所以全初始化为 $1$  

```python
def uniquePaths(m, n):
   # 边界条件 当时边界时只有只有一种方向 = 1
   dp = [[1] * n for _ in range(m)]

   # 状态方程
   for i in range(1, m):
      for j in range(1, n):
            dp[i][j] = dp[i][j-1]+dp[i-1][j]
   return dp[-1][-1]
```

## 机器人在网格中的不同路径2

> 考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径

- 状态方程  
遇到障碍: $dp[i][j] = 0$  
没有障碍: $dp[i][j] = dp[i][j-1]+dp[i-1][j]$
- 边界条件
   1. 当 $obstacleGrid$ 为空时，返回 $0$
   2. 第一行和第一列要要么是 $0$，要么是 $1$
- 遍历
   1. 初始化 $dp$ 和 $dp[0][0]$
   2. 遍历第一行和第一列  
     $dp[j][0] = dp[j - 1][0] * (1 - obstacleGrid[j][0])$
   3. 遍历中间的部分
   4. 用$obstacleGrid$统一起来

```python
def uniquePathsWithObstacles(obstacleGrid):
   if not obstacleGrid:
      return 0
   n = len(obstacleGrid[0])
   m = len(obstacleGrid)
   dp = [[0] * n for _ in range(m)]
   dp[0][0] = 1 - obstacleGrid
   for j in range(1, m):
      dp[j][0] = dp[j - 1][0] * (1 - obstacleGrid[j][0])
   for i in range(1, n):
      dp[0][i] = dp[0][i - 1] * (1 - obstacleGrid[0][i])
   # 状态方程
   for i in range(1, m):
      for j in range(1, n):
            dp[i][j] = (dp[i][j-1]+dp[i-1][j]) * (1 - obstacleGrid[i][j])
   return dp[-1][-1]
```

## 机器人最小路径和

> 给定一个包含非负整数的 $m \cdot n$ 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小

```python
def minPathSum(grid):
   if not grid:
      return 0
   n = len(grid[0])
   m = len(grid)
   for i in range(1, n):
      grid[0][i] += grid[0][i - 1]
   for j in range(1, m):
      grid[j][0] += grid[j - 1][0]
   for x in range(1, m):
      for y in range(1, n):
            grid[x][y] += min(grid[x - 1][y], grid[x][y - 1])
   return grid[-1][-1]
```

## 不同的子序列 115

> 给定一个字符串 S 和一个字符串 T，计算在 S 的子序列中 T 出现的个数。

解法:

- 先写出记录矩阵分析

   ```python
      　    ' ' b  a  b  g  b  a  g
      　' '  1  1  1  1  1  1  1  1
         b   0  1  1  2  2  3  3  3
         a   0  0  1  1  1  1  4  4
         g   0  0  0  0  1  1  1  5
   ```

- 状态  
$dp[i][j]$ 是 $T$ 中前 $i$ 个字符在 $S$ 中前 $j$ 个字符的数目
- 状态转移方程  
   当 $T[i] == S[j]$  
   1. $T[i]$ 与 $S[j]$ 不做匹配：$dp[i][j-1]$  
   2. $T[i]$ 与 $S[j]$ 做匹配：$dp[i-1][j-1]$  

   当 $T[i] \neq S[j]$
   1. $S[i]$ 不起作用：$dp[i][j-1]$
- 边界条件  
  1. 当 $T$ 为空，一直包含，$dp[0][j]=1$
  2. 初始化 $dp$ 要 $+1$

```python
def numDistinct(s, t):
    # n行m列
    # n是t，ｍ是s
    m, n = len(s) + 1, len(t) + 1
    dp = [[0] * m for _ in range(n)]
    for j in range(m):
        dp[0][j] = 1
    # 状态方程
    for i in range(1, n):
        for j in range(1, m):
            if t[i-1] == s[j-1]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
            else:
                dp[i][j] = dp[i][j - 1]
    return dp[n-1][m-1]
```

## 判断子序列

> 给定字符串 s 和 t ，判断 s 是否为 t 的子序列

- 状态
$dp[i][j]$：以第$i$个元素结尾的$S$序列包含以$j$结尾的$T$元素

- 状态转移
  1. 当$S[i]==T[j]$，等价于判断$S[i-1]$是否包含$T[j-1]$
  2. 当$S[i] \neq T[j]$，等价于判断$S[i-1]$是否包含$T[j]$

- 初始化都为True

```python
def isSubsequence(s, t):
    m = len(s) + 1
    n = len(t) + 1
    dp = [[True] * n for _ in range(m)]

    for i in range(1, m):
        dp[i][0] = False

    for i in range(1, m):
        for j in range(1, n):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = dp[i][j-1]

    return dp[m-1][n-1]
```

## 最长回文子串

> 给定一个字符串 s，找到 s 中最长的回文子串

to do