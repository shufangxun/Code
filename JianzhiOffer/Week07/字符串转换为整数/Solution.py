class Solution(object):
    def strToInt(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0
        flag = 1
        str = str.lstrip() # 左边空格全部消除
        if str[0] == '+':
            str = str[1:]
        elif str[0] == '-':
            flag = -1
            str = str[1:]
        res = 0
        i = 0
        while i < len(str):
            if str[i].isdigit():
                res *= 10
                res += int(str[i]) 
                i += 1
            else:
                break
                
        res *= flag
        if res > 2 ** 31 - 1:
             return  2 ** 31 - 1 
        if res < - 2 ** 31:
             return  - 2 ** 31 
        return res 
