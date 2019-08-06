class Solution(object):
    def numberOf1Between1AndN_Solution(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 效率太低 算法复杂度O(n^2)
        s = 0
        for i in range(1, n + 1):
            tmp = i
            while tmp // 10:
                a = tmp % 10
                tmp = tmp // 10
                if a == 1:
                    s += 1
            if tmp == 1:
                s += 1
        return s