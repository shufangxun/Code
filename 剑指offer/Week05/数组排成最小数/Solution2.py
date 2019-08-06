class Solution(object):
    def printMinNumber(self, numbers):
        """使用冒泡进行排序(把最大的放最后)"""
        string = [str(num) for num in numbers]
        flag = True
        count = len(string) - 1
        while flag and count > 0:
            flag = False
            for i in range(len(string)-1):
                if self.theMax(string[i], string[i+1]) == string[i]:
                    temp = string[i]
                    del string[i]
                    string.insert(i+1, temp)
                    flag = True
            count -= 1
        string = ''.join(string)
        return string
        
    def theMax(self, str1, str2):
        '''定义字符串比较函数'''
        return str1 if str1+str2 > str2+str1 else str2
