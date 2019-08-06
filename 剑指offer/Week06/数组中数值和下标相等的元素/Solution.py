class Solution(object):
    def getNumberSameAsIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return -1
        
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] == mid:
                return mid
            elif nums[mid] < mid:
                left = mid + 1
            else:
                right = mid - 1
        return -1