class Solution(object):
    def findNumsAppearOnce(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 得到异或结果
        tmp = 0
        for num in nums:
            tmp ^= num
        # 获取tmp最低位tmp的1
        idx = 0
        while tmp & 1 == 0:
            tmp = tmp >> 1
            idx += 1
        # 分组
        a = b = 0
        for num in nums:
            if (num >> idx) & 1 == 1:
                a ^= num
            else:
                b ^= num
        return [a, b]