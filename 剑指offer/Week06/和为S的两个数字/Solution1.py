class Solution(object):
    def findNumbersWithSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Two sum
        nums = sorted(nums)
        if len(nums) >= 2:
            low, high = 0, len(nums) - 1
            while low < high:
                if nums[low] + nums[high] == target:
                    return [nums[low], nums[high]]
                elif nums[low] + nums[high] < target:
                    low += 1
                else:
                    high += 1
        
        return []

        