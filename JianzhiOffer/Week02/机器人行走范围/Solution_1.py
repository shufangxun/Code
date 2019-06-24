class Solution(object):
    def movingCount(self, threshold, rows, cols):
        """
        :type threshold: int
        :type rows: int
        :type cols: int
        :rtype: int
        """
        # DFS - 类似回溯法，用递归--栈实现
        target = [False] * rows * cols
        if threshold < 0 or rows < 0 or cols < 0:
            return 0
        else: 
            return dfs(threshold, 0, 0)
    
    def sumxy(x, y):
        return x % 10 + y % 10 + x / 10 + y / 10
        
    
    def dfs()