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
        while n >= 0:
            k += 1
            n -= int(k * 10 ** k * 0.9)
        
        if k == 1:
            n += k * 10 ** k
            t = 0
            final = n
        else:
            n += int(k * 10 ** k * 0.9)
            # 从 10 ^ (k-1) 开始s个数
            s = n // k 
            t = n % k 
            final = 10 ** (k - 1) + s
    
        # 再数 t 位

        u = str(final)
        digit = list(map(int, u))[t]  
        return digit
        
     
        



           