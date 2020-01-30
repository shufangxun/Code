class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) <= 0: return 0
        heights = [0] * len(matrix[0])
        maxArea = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == '1':
                    heights[col] += 1
                else:
                    heights[col] = 0
            maxArea = max(maxArea, self.largestRectangleArea(heights))
        return maxArea

    # 调用柱状图最大矩形面积
    def largestRectangleArea(self, heights: List[int]) -> int:
        if heights is None or len(heights) == 0: return 0
        leftLessMin, rightLessMin = [0] * len(heights), [0] * len(heights)
        maxArea = 0
        # 初始化
        leftLessMin[0], rightLessMin[-1] = -1, len(heights)
        # 左边
        for i in range(1, len(heights)):
            p = i - 1
            while p >= 0 and heights[p] >= heights[i]:
                p = leftLessMin[p]
            leftLessMin[i] = p
        # 右边
        for i in range(len(heights) - 2, -1, -1):
            p = i + 1
            while p <= len(heights) - 1 and heights[p] >= heights[i]:
                p = rightLessMin[p]
            rightLessMin[i] = p

        for i in range(len(heights)):
            maxArea = max(maxArea, heights[i] * (rightLessMin[i] - leftLessMin[i] - 1))
        return maxArea
