# DFS
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        visited = [[0] * n for _ in range(m)]
        self.dfs(visited, 0, 0, m, n, k)
        return sum(map(sum, visited))


    def dfs(self, visited, i, j, m, n, k):
        if not 0 <= i <= m - 1 or  not 0 <= j <= n - 1 or \
            self.sumbit(i) + self.sumbit(j) > k or visited[i][j] == 1:
            return

        visited[i][j] = 1

        self.dfs(visited, i, j+1, m, n, k)
        self.dfs(visited, i, j-1, m, n, k)
        self.dfs(visited, i+1, j, m, n, k)
        self.dfs(visited, i-1, j, m, n, k)
        

    def sumbit(self, a):
        val = 0 
        while a:
            val += a % 10 
            a = a // 10
        return val

class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        visited = set([(0, 0)])
        for i in range(m):
            for j in range(n):
                if ((i-1, j) in visited or (i, j-1) in visited) and self.sumbit(i) + self.sumbit(j) <= k:
                    visited.add((i, j))
        return len(visited)

    def sumbit(self, a):
        val = 0 
        while a:
            val += a % 10 
            a = a // 10
        return val 

