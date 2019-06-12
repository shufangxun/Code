class Solution(object):
    def duplicateInArray(self, nums):
        """
        :type nums: List[int]
        :rtype int
        hash法 开辟空间存数组，当hash table内没有时，数目+1，否则输出
        时间复杂度： O(n)
        空间复杂度： O(n)
        """
        
        hashmap = {}
        
        if nums == [] or max(nums) >= len(nums) or min(nums) <= -1: # 异常处理
            return -1   
        
        else:
            for i in range(len(nums)):
                if nums[i] not in hashmap.keys():
                    hashmap[nums[i]] = 1
                else:
                    return nums[i]
        return -1  # 不包含重复数字
        
        

                    