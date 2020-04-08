class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        
        # 转置
        for i in range(m):
            for j in range(i + 1):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # 左右翻折
        for i in range(m):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]