class Solution(object):
    def add(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        # 特判
        if num1 == 0 or num2 == 0:
            return max(num1, num2)

        res = 0
        # 进位
        cin = 0
        for i in range(32):
            a = num1 & (1 << i)
            b = num2 & (1 << i)
            # 不进位的和
            s = (a ^ b) ^ cin
            # 下面计算进位，三者之中，任意两者同为 1 的时候，就可以进位
            cin = (a & b) | (a & cin) | (b & cin)
            cin <<= 1
            res += s
            
        # 正负数判断
        if res >> 31 == 0:
            return res
        return res - (1 << 32)

