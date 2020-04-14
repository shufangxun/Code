class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        candidates.sort()
        self.dfs([], candidates, target, res, n, 0)
        return res

    def dfs(self, path, candidates, target, res, n, start):
        if target == 0:
            res.append(path[:])
            return 
        
        for i in range(start, n):
            if i > start and candidates[i-1] == candidates[i]:  #数组常见去重复的方法，对于重复的数值，我们只让第一个进入循环，后面的就不要再进入循环了
                continue

            if target - candidates[i] >= 0:
                path.append(candidates[i])
                self.dfs(path, candidates, target-candidates[i], res, n, i+1)
                path.pop()