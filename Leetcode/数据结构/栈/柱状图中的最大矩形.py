# 暴力法
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        n = len(heights)
        for i in range(n):
            left_i = i
            right_i = i
            while left_i >= 0 and heights[left_i] >= heights[i]:
                left_i -= 1
            while right_i < n and heights[right_i] >= heights[i]:
                right_i += 1
            res = max(res, (right_i - left_i - 1) * heights[i])
        return res
        

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
 
# 单调栈
class Solution1:
    def largestRectangleArea(self, heights: List[int]):
        S = []
        area = 0
        heights = [0] + heights + [0]
        for i in range(len(heights)):
            while S and heights[S[-1]] > heights[i]: 
            area = max(area, heights[S.pop()] * (i - S[-1] - 1))
            S.append(i)
        return area  

class Solution2:
    def largestRectangleArea(self, heights: List[int]):
        S = [-1]
        area = 0
        for i in range(len(heights)):
            while S[-1] != -1 and heights[S[-1]] > heights[i]: 
                area = max(area, heights[S.pop()] * (i - S[-1] - 1))
            S.append(i)
        while S[-1] != -1:
            area = max(area,  heights[S.pop()] * (len(heights)-S[-1]-1))
        return area



