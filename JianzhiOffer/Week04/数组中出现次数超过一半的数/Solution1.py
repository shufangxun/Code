class Solution(object):
    def moreThanHalfNum_Solution(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # hashmap法
        hash = dict()
        for num in nums:
            if num in hash.keys():
                hash[num] += 1
            else:
                hash[num] = 1
            if hash[num] > len(nums) / 2:
                return num
        
        