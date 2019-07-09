class Solution(object):
    def NumberOf1(self,n):
        """
        :type n: int
        :rtype: int
        """
        # 循环32次
        # 所以最高位补什么都没事
        count = 0
        for _ in range(32):
            count += n & 1
            n = n >> 1
        return count
