class Solution(object):
    def getNumberOfK(self, nums, k):
        """
        :type nums: list[int]
        :type k: int
        :rtype: int
        """
        count = dict()
        for num in nums:
            if num in count.keys():
                count[num] += 1
            else:
                count[num] = 1
        
        if k in count.keys():
            return count[k]
        else:
            return 0