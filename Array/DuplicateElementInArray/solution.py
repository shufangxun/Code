class Solution(object):
    def duplicateInArray(self, nums):
        """
        :type nums: List[int]
        :rtype int
        """
        hashmap = {}
        
        if nums == [] or (max(nums) > (len(nums) - 1)):
            return -1   
        
        else:
            for i in range(len(nums)):
                if nums[i] < 0:
                    return -1
                if nums[i] not in hashmap.keys():
                    hashmap[nums[i]] = 1
                else:
                    return nums[i]
        return -1  # 不包含重复数字
                    