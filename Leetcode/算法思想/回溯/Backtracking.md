# 回溯

回溯实际上是一个决策树的遍历过程，都思考3个问题：
- 路径：已经做出的选择
- 选择列表：当前可以做的选择
- 结束条件：到达决策树底层，无法再做选择的条件

整体框架如下
```python
result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return
    
    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择
```

### 46. 全排列 I

> 给定一个没有重复数字的序列，返回其所有可能的全排列

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        used, res = [False] * len(nums), []
        self.DFS(nums, 0, [], used, res)
        return res
    def DFS(self, nums, index, pre, used, res):
        # 满足条件时，保存一个结果
        if index == len(nums):
            res.append(pre.copy())
            return
        for i in range(len(nums)):
            if not used[i]:
                used[i] = True
                pre.append(nums[i])
                # 继续搜索
                self.DFS(nums, index+1, pre, used, res)
                #回溯时要记得状态重置
                used[i] = False
                pre.pop()
```

### 全排列 II

> 给定一个可包含重复数字的序列，返回所有不重复的全排列

思路

- 在开始回溯算法之前，对数组进行一次排序操作；
- 在进入一个新的分支之前
  - 当前这个数是否和前一个数相等(也就是当前已选数与同一层前一分支已选数相等)
  - 之前的数在当前分支还未使用
- 那么接下来如果走这个分支，就会发生重复，此时分支和之前的分支一模一样

```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0: 
            return []
        nums.sort()
        used, res = [False] * len(nums), []
        self.DFS(nums, 0, [], used, res)
        return res
    def DFS(self, nums, index, pre, used, res):
        # 满足条件时，保存一个结果
        if index == len(nums):
            res.append(pre.copy())
            return
        for i in range(len(nums)):
            if not used[i]:
                # 这个数和之前的数一样，并且之前的数还未使用过，那接下来如果走这个分支，就会使用到之前那个和当前一样的数，就会发生重复
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                pre.append(nums[i])
                # 继续搜索
                self.DFS(nums, index+1, pre, used, res)
                #回溯时要记得状态重置
                used[i] = False
                pre.pop()
```

### 22. 括号生成

> 给出n代表生成括号对数，给出所有括号情况

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.dfs("", res, n, n)
        return res

    def dfs(self, sublist, res, left, right):
        if left == 0 and right == 0:
            res.append(sublist)
        if right < left:
            return
        if left > 0:
            self.f(sublist + '(', res, left-1, right)
        if right > 0:
            self.f(sublist + ')', res, left, right-1)
```
