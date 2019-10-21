class Solution(object):
    def int2bit(self, num):
        return (bin(((1 << 32) - 1) & i)[2:]).zfill(32)
        
    def bit2int(self, byte):
        return int(byte[1:], 2) - int(byte[0]) * (1 << 31)   

    def add(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        # 应该用补码表示
        res, Cin = 0, 0
        bitextra = 1  # 提取每个位置的bit用的
        bnum1 = list(map(int, self.int2bit(num1))) # 转换为数字
        bnum2 = list(map(int, self.int2bit(num2)))
        for i in range(32):
            a = num1 & bitextra
            b = num2 & bitextra
            S = (a^b)^Cin  # 当        前输出位
            Cout = a & b | a & Cin | b & Cin
            Cin = Cout << 1 # 2倍操作
            bitextra <<= 1
            res += S
        
        return res

        
            



