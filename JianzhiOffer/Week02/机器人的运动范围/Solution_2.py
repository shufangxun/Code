class Solution(object):
    def movingCount(self, threshold, rows, cols):
        """
        :type threshold: int
        :type rows: int
        :type cols: int
        :rtype: int
        """
        self.memo = {}
        self.m = rows
        self.n = cols
        self.k = threshold
        return self.dfs(0, 0)

    def get_sum(self, x):
        res = 0
        while x:
            res += x % 10
            x = x//10
        return res 
    def is_valid(self, x, y):
        return 0 <= x < self.m and 0 <= y < self.n and self.get_sum(x) + self.get_sum(y) <= self.k     

    def dfs(self, x, y):
        if not self.is_valid(x, y):
            return 0
        if (x,y) in self.memo:
            return 0
        self.memo[(x,y)] = 1
        return self.dfs(x-1, y) + self.dfs(x, y-1) + self.dfs(x+1, y) + self.dfs(x, y+1) + 1
