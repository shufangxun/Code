# 暴力法
class Solution1:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 得到高度种类
        heightCount = set(heights)
        maxArea = 0
        for h in heightCount:
            width, maxWidth = 0, 1
            # 找连续的高于h的柱
            for i in range(len(heights)):
                if heights[i] > h:
                    width += 1
                else:
                    maxWidth = max(maxWidth, width)
                    width = 0
            # 更新最大面积
            maxWidth = max(width, maxWidth)
            maxArea = max(maxArea, h * maxWidth)
        return maxArea

# 优化 中心扩散
class Solution2:
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


