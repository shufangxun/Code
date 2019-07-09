class Solution(object):
    def Power(self, base, exponent):
        """
        :type base: float
        :type exponent: int
        :rtype: float
        """
        # 递归
        try:
            res = self.helper(base, abs(exponent))
            if exponent < 0:
                return 1.0 / res
                            
        except ZeroDivisionError:
            print('Error: base is zero')
        else:
            return res
        
        

    def helper(self, base, exponent):
        
        # base case
        if exponent == 0:
            return 1
        if exponent == 1:
            return base 

        # 递归
        res = self.helper(base, exponent >> 1)
        res *= res

        # 指数为奇, 要再乘一个base
        if exponent & 1 == 1: 
            res *= base
        
        return res