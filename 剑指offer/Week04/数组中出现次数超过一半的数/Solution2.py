class Solution(object):
    def moreThanHalfNum_Solution(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        res = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if count == 0:
                res = nums[i]
                count = 1
            elif nums[i] == res:
                count += 1
            else:
                count -= 1
        
        check = 0
        for i in range(len(nums)):
            if nums[i] == res:
                check += 1
        
        return res if check * 2 > len(nums) else 0
            