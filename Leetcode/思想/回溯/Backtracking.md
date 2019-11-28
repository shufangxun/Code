# 回溯

## 全排列

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
        if len(nums) == 0: return []
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
