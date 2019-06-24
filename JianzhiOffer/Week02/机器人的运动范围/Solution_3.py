from collections import deque
class Solution(object):
    def movingCount(self, threshold, rows, cols):
        """
        :type threshold: int
        :type rows: int
        :type cols: int
        :rtype: int
        """
        if not rows or not cols:
            return 0
        res = 1
        memo = set()
        memo.add((0,0))
        q = deque([(0,0)])
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        while q:
            x, y = q.popleft()
            for i in range(4):
                xx = x + dx[i]
                yy = y + dy[i]
                if self.is_valid(xx, yy, rows, cols, threshold) and (xx, yy) not in memo:
                    res += 1
                    q.append((xx, yy))
                    memo.add((xx, yy))
        return res

    def is_valid(self, x, y, m, n, k):
        return 0 <= x < m and 0 <= y < n and self.sumxy(x, y) <= k

    def sumxy(self, x, y):      
        return x % 10 + x // 10 + y % 10 + y // 10

 