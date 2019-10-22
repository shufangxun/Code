class Solution(object):
    def add(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        while num2:
            s = num1 ^ num2
            c = num1 & num2
            num1 = s & 0xFFFFFFFF
            num2 = c << 1

        if num1 >> 31 == 0:
            return num1
        # 如果是负数
        return num1 - (1 << 32)

        
            



