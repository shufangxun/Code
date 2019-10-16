class Solution(object):
    def getMissingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        if end < 0:
            return 0
        if end == nums[end]:　　# 形如 [0,1,2,3]
            return end + 1
        while start < end:
            mid = (start + end) >> 1
            if nums[mid] == mid:
                start = mid + 1  # 缺失的在后半段
            else:
                end = mid # 缺失的在前半段

        return nums[end] - 1