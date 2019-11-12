class Solution(object):
    def findContinuousSequence(self, sum):
        """
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        low, high = 1, 2
        while low < high:
            # 计算当前和: 等差数列
            curSum = (low + high) * (high - low + 1) // 2
            if curSum == sum:
                elem = []
                for i in range(low, high+1):
                    elem.append(i)
                res.append(elem)
                low += 1 # 细节
            elif curSum < sum:
                high += 1
            else:
                low += 1
        return res

