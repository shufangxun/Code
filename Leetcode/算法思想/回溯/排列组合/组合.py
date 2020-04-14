class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        if n == 0 or k == 0:
            return []

        self.dfs([], n, k, 1, res)
        return res

    def dfs(self, path, n, k, start, res):
        if len(path) == k:
            res.append(path[:])
            return
        
        for i in range(start, n + 1):
            path.append(i)
            # 去重
            self.dfs(path, n, k, i + 1, res)
            path.pop()
        