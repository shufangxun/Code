class Solution(object):
    def NumberOf1(self,n):
        """
        :type n: int
        :rtype: int
        """
        # 循环k次
        # k是n中1的个数
        count = 0
        if n<0:
            n =  n & 0xffffffff 
        while n:
            n = n & (n-1)
            count += 1
        return count