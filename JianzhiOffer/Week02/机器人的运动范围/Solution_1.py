class Solution:

    # DFS - 递归法
    def movingCount(self, threshold, rows, cols):
        visit = [[False for i in range(cols)] for j in range(rows)]
        return self.dfs(threshold, rows, cols, visit, 0, 0)
      
    def judge(self, threshold, x, y):
        if sum(map(int,str(ｘ) + str(y))) <= threshold: # 精髓
            return True
        else:
            return False
        
    def dfs(self, threshold, rows, cols, visit, x, y):
        count = 0
        if x < rows and x >= 0 and y < cols and y >= 0 and self.judge(threshold, x, y) and visit[x][y] == False:
            visit[x][y] = True
            # visit数组一直传参下去,保证了变化能够更新
            count = 1+ self.dfs(threshold, rows, cols, visit, x-1, y) \
                    + self.dfs(threshold, rows, cols, visit, x+1, y) \
                    + self.dfs(threshold, rows, cols, visit, x, y-1) \
                    + self.dfs(threshold, rows, cols, visit, x, y+1)
        return count

