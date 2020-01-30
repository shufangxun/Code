# 路径

## 爬楼梯方式

> 需要 $n$ 阶才能到达楼顶，每次可以爬 $1$ 或 $2$ 个台阶。请问有多少种不同的方法可以爬到楼顶

思路

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

思路

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

思路

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
