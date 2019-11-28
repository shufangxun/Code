# 回溯

## 全排列 I

> 给定一个没有重复数字的序列，返回其所有可能的全排列

思路

- 定义 used 数组
  保证上一层选过的数字不在下一层出现，使用一个数组长度这么长的额外空间
- 栈弹出回溯
  - 释放对最后一个数的占用
  - 将最后一个数从当前选取的排列中弹出

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

## 全排列 II

> 给定一个可包含重复数字的序列，返回所有不重复的全排列

思路

- 在开始回溯算法之前，对数组进行一次排序操作；
- 在进入一个新的分支之前，看这个数是不是和之前的数一样，如果这个数和之前的数一样，并且之前的数还未使用过，那接下来如果走这个分支，就会使用到之前那个和当前一样的数，就会发生重复，此时分支和之前的分支一模一样。（这句话特别关键，可以停下来多看两遍，再看一看上面画的那张图）

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
