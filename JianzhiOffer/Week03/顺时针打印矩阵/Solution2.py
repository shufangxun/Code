class Solution(object):
    def printMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        
        res = []
        r = len(matrix)
        if r == 0:
            c = 0
        else:
            c = len(matrix[0])
            
        if matrix == [] or r <= 0 or c <= 0:
            return res
        
        

        start = 0 
        
        while r > 2 * start and c > 2 * start:  # 起始点
            res.extend(self.OneCycle(matrix , r, c, start))
            start += 1   # 到下个循环起始点
        
        return res

    def OneCycle(self, matrix, rows, columns, start):
        res = []
        
        # 到达列号和行号
        endX = columns - start -1
        endY = rows - start - 1

        # 从左往右 : 第start行,从start到endX列
        for i in range(start, endX + 1):
            res.append(matrix[start][i])
	

        # 从上到下: 第endX列, 从第start + 1行到endY行
        if start < endY:
            for i in range(start + 1, endY + 1):
                res.append(matrix[i][endX])
        
        # 从右往左: 第endY行, 从第endX - 1列到第start列
        if start < endY and start < endX:
            for i in range(endX - 1, start - 1, -1):
                res.append(matrix[endY][i])

        # 从下到上: 第start列, 从第endY - 1行到第start - 1行
        if start < endY - 1 and start < endX:
            for i in range(endY - 1, start, -1):
                res.append(matrix[i][start])

        return res