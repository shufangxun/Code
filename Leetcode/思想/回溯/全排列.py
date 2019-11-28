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
