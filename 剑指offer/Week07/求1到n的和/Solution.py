class Solution(object):
    def getSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = n
        tmp = n > 0 and  self.getSum(n - 1)
        res += tmp
        return res    


        # 爆栈