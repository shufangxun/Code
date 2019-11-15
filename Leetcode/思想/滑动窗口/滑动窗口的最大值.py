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
            # 在尾部添加元素，并保证左边元素都比尾部大
            while window and nums[window[-1]] < num:
                window.pop(-1)
            window.append(i)
            # 当长度大于k时,弹出队首元素
            if window[0] == i - k:
                window.pop(0)
            if i >= k - 1:
                res.append(nums[window[0]])
        return res