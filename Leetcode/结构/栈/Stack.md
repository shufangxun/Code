# 栈

## 柱状图中最大的矩形

[参考](https://leetcode.wang/leetCode-84-Largest-Rectangle-in-Histogram.html)

> 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。求在该柱状图中，能够勾勒出来的矩形的最大面积。

```txt
输入: [2,1,5,6,2,3]
输出: 10
```

法1：暴力法

- 时间复杂度；$O(N^{2})$
- 空间复杂度：$O(N)$

思路：找出所有高度下的最大矩形面积，选出最大的即可

- 首先存储高度 h
- 找连续的大于等于 h 的柱形个数 n
- 最大面积即为 n * h

```python
def largestRectangleArea(heights):
    # 得到高度种类
    heightCount = set(heights)
    maxArea = 0
    for h in heightCount:
        width, maxWidth = 0, 1
        # 找连续的高于 h 的柱
        for i in range(len(heights)):
            if heights[i] >= h:
                width += 1
            else:
                maxWidth = max(maxWidth, width)
                width = 0
        # 更新最大面积
        maxWidth = max(width, maxWidth)
        maxArea = max(maxArea, h * maxWidth)
    return maxArea
```

法2：中心扩散

思路：求出包含每个柱子的最大面积，然后选出最大的

- 遍历每个柱子，只需找到比其矮的左侧第一个 leftLessMin 和右侧矮的第一个 rightLessMin，就可求出矩形的面积为 (rightLessMin - leftLessMin - 1) * 当前柱子高度。
- 如何找这两个是关键
  - $O(N^{2})$ 做法：用两个数组保存每一个柱子左侧或右侧第一个小的柱子

    ```python
    leftLessMin[0] = -1
    for i in range(1, len(heights)):
        p = i - 1
        while p >= 0 and heights[p] >= heights[i]:
            p -= 1
        leftLessMin[i] = p
    ```

  - $O(N)$ 做法：当前柱子 i 比上一个柱子 i-1 矮的时候，直接比较 leftLessMin[i - 1] 和 当前柱子 i 
    - 因为柱子 i-1 高于 柱子 i，那么从第一个比 i-1 矮的柱子的后一个柱子到柱子 i-1 都是比柱子 i 高的，不需要比较，直接跳过
    - 只要改一行!

    ```python
    leftLessMin[0] = -1
    for i in range(1, len(heights)):
        p = i - 1
        while p >= 0 and heights[p] >= heights[i]:
            p = leftLessMin[p]
        leftLessMin[i] = p
    ```

完整代码:

```python

def largestRectangleArea(heights):
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
```

法3：用栈做

- 时间复杂度：$O(N)$
- 空间复杂度：$O(N)$

```python

def largestRectangleArea(heights):
    heights.append(0)
    stack = [-1]
    ans = 0
    for i in range(len(heights)):
        while heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i - stack[-1] - 1
            ans = max(ans, h * w)
        stack.append(i)
    heights.pop()
    return ans
```
