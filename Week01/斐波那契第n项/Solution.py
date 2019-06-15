class Solution(object):
    def Fibonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n > 1:
            return self.Fibonacci(n - 1) + self.Fibonacci(n - 2)
        '''
        if n == 0: 
            return 0

        a, b = 0, 1
        while n - 1:
            a, b = b, a + b
            n -= 1
        
        return b