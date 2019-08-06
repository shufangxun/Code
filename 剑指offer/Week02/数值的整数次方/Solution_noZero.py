class Solution(object):
    def Power(self, base, exponent):
        """
        :type base: float
        :type exponent: int
        :rtype: float
        """
        # 不同时为0
        flag = True
        if exponent < 0:
            flag = False

        res = 1   
        exponent = abs(exponent)
        while exponent > 0:
            res *= base
            exponent -= 1
        if flag == False:
            res = 1 / res
        
        return res
        
