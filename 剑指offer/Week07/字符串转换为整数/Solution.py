class Solution(object):
    def strToInt(self, s):
        """
        :type str: str
        :rtype: int
        """
        if not s:
            return 0

        flag = 1
        res = 0
        nums = {str(i) for i in range(10)} # 集合解析
        s = s.lstrip()

        # 只显式讨论这两种
        # 首位不是数字和+.-,实际上就是返回0
        # 首位是数字,下面直接操作,不需要从1开始
        if s[0] == '+':
            s = s[1:]
        elif s[0] == '-':
            s = s[1:]
            flag = -1
        
        for i in s:
            if i in nums:
                res *= 10
                res += int(i)
            else:
                break

        res *= flag

        if res > 2 ** 31 - 1:
             return  2 ** 31 - 1 
        if res < - 2 ** 31:
             return  - 2 ** 31 
        return res
        