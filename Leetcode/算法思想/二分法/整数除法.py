'''
思路就是减去除数，统计可以减去多少个，为了加速计算，减去多少个这个部分用位移加速
1. a << b 相当于 a * 2^b，a >> b 相当于 a // 2^b
2. 异或操作 ^ 可以判断俩数字是否异号
'''


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        dvd, div = abs(dividend), abs(divisor)
        res = 0
        INT_MAX, INT_MIN = pow(2, 31) - 1, -pow(2, 31)

        while dvd >= div:
            cnt, base = 1, div
            while dvd > (base << 1):
                cnt <<= 1 # cnt * 2: 做了多少次减法
                base <<= 1 # base * 2
            res += cnt
            dvd -= base # 减完之后再次判断是否 dvd >= div
            
        res = res if (dividend < 0) ^ (divisor < 0) == 0 else -res
        return INT_MAX if res > INT_MAX or res < INT_MIN else res