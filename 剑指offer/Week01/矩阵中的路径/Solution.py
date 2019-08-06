class Solution(object):
    def hasPath(self, matrix, string):
        """
        :type matrix: List[List[str]]
        :type string: str
        :rtype: bool
        """
        if matrix == []:
            return False

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                # 遍历搜素每一个点与str的匹配关系
                if self.dfs(matrix, string, 0, i, j):
                    return True 
        
        return False

    def dfs(self, matrix, string, p, x, y):
        '''
        p: 字符串字符坐标
        x,y: 矩阵的点坐标
        '''
        # 回溯法模版
        # 出口
        memo = matrix[x][y]
        if matrix[x][y] != string[p]:  # 这个要好好理解
            return False
        if p == len(string) - 1:  # 这个必须在后面,先判断是否相等 [['a','a']] 'aaa'
            return True
        
        # 上面操作顺利,不返回,则说明[x][y]是符合条件

        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        
        matrix[x][y] = '*'

        # 查找周围节点
        for i in range(4):
            x_new = x + dx[i]
            y_new = y + dy[i]

            if x_new >= 0 and x_new < len(matrix) and y_new >= 0 and y_new < len(matrix[0]):
                if self.dfs(matrix, string, p + 1, x_new, y_new):
                    return True   # 意思是四个里面找到一个就返回True
    
        matrix[x][y] = memo
        return False 


        