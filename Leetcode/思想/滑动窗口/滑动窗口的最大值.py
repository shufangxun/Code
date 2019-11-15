class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) < k:
            return []
        window, res = [], []
        for i, num in enumerate(nums):
            if i >= k and window[0] <= i - k:
                window.pop(0)
            while window and num >= nums[window[-1]]:
                window.pop(-1)
            window.append(i)
            if i >= k - 1:
                res.append(nums[window[0]])
        return res