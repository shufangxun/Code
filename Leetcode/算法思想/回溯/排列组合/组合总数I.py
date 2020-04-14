class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        # 剪枝
        candidates.sort()
        self.dfs([], candidates, target, res, n, 0)
        return res

    def dfs(self, path, candidates, target, res, n, start):
        if target == 0:
            res.append(path[:])
            return 
        
        for i in range(start, n):
            if target - candidates[i] >= 0:
                path.append(candidates[i])
                self.dfs(path, candidates, target-candidates[i], res, n, i)
                path.pop()
            '''
            剪枝
            if target - candidates[i] < 0:
                break
            path.append(candidates[i])
            self.dfs(path, candidates, target-candidates[i], res, n, i)
            path.pop()
            '''