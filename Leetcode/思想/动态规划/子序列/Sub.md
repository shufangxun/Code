# 子序列

## 最长上升子序列

> 给定一个无序的整数数组，找到其中最长上升子序列的长度

法1：朴素动态规划

- 状态定义
$dp[i]$：前 i 个数字的最长子序列长度
- 状态转移
$dp[i] = max(dp[i], dp[j] + 1)$
- 初始化和循环
初始化为1，两重循环，第一重是 i，第二重是找 i 中的 j
- 复杂度分析
  - 时间：$O(N^{2})$
  - 空间：$O(N)$

```python
def LIS1(nums):
    if len(nums) <= 1: return len(nums)
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
```

法2：二分法优化

- 贪心思路
如果前面的数越小，后面接上一个随机数，就会有更大的可能性构成一个更长的上升子序列
- 二分法
降低内层找元素的时间复杂度：由 $O(N)$ 降低到 $O(logN)$
- 保证严格递增
新建队列 Queue，用于保存最长上升子序列；然后对原数组进行遍历，将每位元素二分插入 cell 中
  - 如果 Queue 中元素都比它小，将它插入队尾
  - 否则，用它覆盖掉比它大的元素中最小的那个

```python
def LIS2(nums):
    if len(nums) <= 1: return len(nums)
    Queue = [nums[0]]
    for i in range(1, len(nums)):
        # 插入队尾
        if nums[i] > Queue[-1]:
            Queue.append(nums[i])
        else:
            l, r = 0, len(nums) - 1
            while l < r:
                mid = l + (r - l) // 2
                if nums[mid] < nums[i]: l = mid + 1
                else: r = mid
            Queue[l] = numm[i]
    return len(Queue)
```

## 最长公共子序列 

> 求两个序列的最长公共部分

- 状态
$dp[i][j]$：序列 S 前 i 部分和序列 T 前 j 部分的最长公共子序列部分 
- 状态转移
  - S[i] == T[j]
    $dp[i][j] = dp[i - 1][j - 1] + 1$ 
  - S[i] != T[j]
    $dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])$
- 初始化和循环
  两重循环，初始化要 +1 长度，因为有空数组

```python
def LCS(s1, s2):
    m = len(s1)
    n = len(s2)
    dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]
```


## 不同的子序列 115

> 给定一个字符串 S 和一个字符串 T，计算在 S 的子序列中 T 出现的个数。

思路

- 先写出记录矩阵分析

   ```python
      　    ' ' b  a  b  g  b  a  g
      　' '  1  1  1  1  1  1  1  1
         b   0  1  1  2  2  3  3  3
         a   0  0  1  1  1  1  4  4
         g   0  0  0  0  1  1  1  5
   ```

- 状态  
$dp[i][j]$ 是 $T$ 中前 $i$ 个字符在 $S$ 中前 $j$ 个字符的次数
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

> 给定字符串 S 和 T ，判断 S 是否为 T 的子序列

思路

- 状态
$dp[i][j]$：以第 $i$ 个元素结尾的 $S$ 序列包含以 $j$ 结尾的 $T$ 元素

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

## 连续子数组最大和

> 给定一个整数数组 $nums$ ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和

思路：除了状态转移，还要看怎么遍历

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

## 最长回文子串 [参考](https://leetcode-cn.com/problems/longest-palindromic-substring/solution/zhong-xin-kuo-san-dong-tai-gui-hua-by-liweiwei1419/)  

> 给定一个字符串 s，找到 s 中最长的回文子串

```python
输入: "cbbd"
输出: "bb"
```

法1. 朴素动态规划

- 时间复杂度：$O(n^{2})$
- 空间复杂度：$O(n^{2})$

- 状态  
$dp[i][j]$；二维布尔数组，当字符串 $s[i:j]$ 是回文串，则为 True，否则为 False

- 状态转移
  - 第一步是如何选取子序列  
     遍历即可，用 left 和 right 两个指针
  - 判断  
      如果子串 $s[left][right]$ 边界 $s[left] == s[right]$ ，那么将考察这个子串向中间收缩一个字符(**如果可以的话**)的情况，也就是 $s[left + 1][right - 1]$

    - 可以收缩($len > 3$)  
       左右边界字符串相等的时候，原字符串是否回文就**完全**由＂**原字符串去掉左右边界**＂的子串是否回文决定
    - 不可收缩($len <= 3$)  
       当长度为3或2时，收缩之后长度为1和0，收缩情况状态转移不适用，**只要左右边界相等就是回文串**
       1. 当原字符串长度为3时，如果左右边界的字符相同，去掉左右边界的子串长度则为1，它一定是回文串，则原字符串也**一定是回文串**。
       2. 当原字符串长度为2时，如果左右边界的字符相同，去掉左右边界的子串长度则为0，**显而易见原字符串是一个回文串**
    - 方程

      ```python
      dp[l][r] = (s[l] == s[r] and (r - l <= 2 or dp[l + 1][r - 1]))
      ```

```python
def longestPalindrome(s):
   if len(s) < 2:
      return s
   # 初始化为False
   dp = [[False for _ in range(len(s))] for _ in range(len(s))]
   # 偷懒：若是回文子串长度为1，返回第一个字符就行
   maxlen, res = 1, s[0]
   for right in range(1, len(s)):
      for left in range(right):
            # 包含长度为1和2的情况 关键所在
            # 在左右边界字符相等的前提下，如果收缩后不构成区间（最多只有 1 个元素），直接返回 True
            if s[left] == s[right] and (right - left <= 2 or dp[left + 1][right - 1]):
               dp[left][right] = True
               curlen = right - left + 1
               if curlen > maxlen:
                  maxlen = curlen
                  res = s[left : right + 1]
   return res
```

法2. 中心扩散 优化空间

- 时间复杂度：$O(N^{2})$  
  **枚举中心**时间复杂度为 $O(N)$，从中心扩散得到回文子串的时间复杂度为 $O(N)$，因此时间复杂度可以降到 $O(N^{2})$
- 空间复杂度：$O(1)$  
  只使用到常数个临时变量，与字符串长度无关

思路：遍历每一个索引，以这个索引为中心，利用回文串**中心对称**的特点，往两边扩散，看最多能**扩散多远**

- 中心点选取  
回文串在长度为奇数和偶数的时候，回文中心不一样：
   1. 奇数回文串的中心是一个**具体的字符**
   2. 偶数回文串的中心是位于中间的**两个字符的空隙**  

   每次循环选择一个中心，进行左右扩展，判断左右字符是否相等，共有 $n + n - 1$ 个回文串中心

- 扩散
  1. 如果传入重合的索引，得到的回文子串的长度是奇数；  
  2. 如果传入相邻的索引，得到的回文子串的长度是偶数

```python
class Solution2:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        maxlen, res = 1, s[0]
        for i in range(len(s)):
            odd, lenodd = self.spreadCenter(s, i, i)
            even, leneven = self.spreadCenter(s, i, i + 1)
            curS = odd if lenodd >= leneven else even
            if len(curS) > maxlen:
                maxlen = len(curS)
                res = curS
        return res
    def spreadCenter(self, s, i, j):
        left, right = i, j
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1 : right], right - left - 1
```
