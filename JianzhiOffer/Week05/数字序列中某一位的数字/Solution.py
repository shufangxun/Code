class Solution(object):
    def digitAtIndex(self, n):
        """
        :type n: int
        :rtype: int
        """

        # k是位数: 个位,十位,百位
        
        if n < 0:
            return 
        
        k = 1
        n -= k * 10 ** k
        while n:
            k += 1
            n -= k * 10 ** k
        # 此时 n是负数 , k是下一个开始的位数
        n += k * 10 ** k
        # 从 10 ^ (k-1) 开始s个数
        s = n // k 
        t = n % k 
        final = 10 ** (k - 1) + s - 1
        # 再数 t 位

        while t > 0:
            final = final // 10
            t -= 1

        return final 
        

     
        



           