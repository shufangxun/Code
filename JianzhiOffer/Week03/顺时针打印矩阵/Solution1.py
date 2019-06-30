class Solution(object):
    def printMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # 用zip()很简单,但不利于考察
        res = []
        while matrix:
            res.extend(matrix[0])
            matrix = list(zip(*matrix[1:]))  # 迭代从每一个列表里取一个元素组成新的列表,组成新的矩阵
            matrix = matrix[::-1]  # 从后往前重新排列矩阵

        return res

