class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cursum = nums[0]
        maxsum = cursum
        for i in range(1, len(nums)):
            cursum = max(0, cursum) + nums[i]
            if cursum > maxsum:
                maxsum = cursum
        return maxsum