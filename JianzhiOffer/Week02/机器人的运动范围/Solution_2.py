class Solution(object):
    def movingCount(self, threshold, rows, cols):
        """
        :type threshold: int
        :type rows: int
        :type cols: int
        :rtype: int
        """
        # 构建一个空字典存放标记
        self.memo = {}
        self.m = rows
        self.n = cols
        self.k = threshold
        return self.dfs(0, 0)

    def sumxy(self, x, y):      
        return x % 10 + x // 10 + y % 10 + y // 10

    def is_valid(self, x, y):
        return 0 <= x < self.m and 0 <= y < self.n and self.sumxy(x, y) <= self.k     

    def dfs(self, x, y):
        if not self.is_valid(x, y) and (x, y) in self.memo:
            return 0
            
        self.memo[(x,y)] = 1
        return self.dfs(x-1, y) + self.dfs(x, y-1) + self.dfs(x+1, y) + self.dfs(x, y+1) + 1
