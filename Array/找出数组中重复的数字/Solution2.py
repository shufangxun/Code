class Solution(object):
    def duplicateInArray(self, nums):
        """
        :type nums: List[int]
        :rtype int
        思想是把每个数放到对应的位置上，即让 nums[i] = i 
        时间复杂度： O(n)
        空间复杂度： O(1)
        """
        
        
        if nums == [] or max(nums) >= len(nums) or min(nums) <= -1: # 异常处理
            return -1   
        
        
        for i in range(len(nums)):
            
            while nums[i] != i:   # x != i
                if nums[nums[i]] == nums[i]:  ## nums[i] = x && nums[x] = x
                    return nums[i] 
                else:
                    nums[nums[i]], nums[i] =  nums[i], nums[nums[i]]
                    
                
        return -1  # 不包含重复数字


if __name__ == "__main__":
    arr = list([1,2,3,1,4])
    A = Solution()
    A.duplicateInArray(arr)