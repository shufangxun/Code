class Solution(object):
    def printMinNumber(self, nums):
        # write code here
        if not nums:
            return ""  # 返回字符0

        res = []  # 存放所有可能排序
        path = "" # 路径
        tmp = [str(x) for x in nums]
        self.helper(tmp, res, path)
        return min(res)   # 返回最小值
    

    def helper(self, str, res, path):
        if not str:
            res.append(int(path)) #　转换为int
        else:
            for i in range(len(str)):    # 遍历 9*8*7*....
                self.helper(str[:i] + str[i+1:], res, path + str[i])
