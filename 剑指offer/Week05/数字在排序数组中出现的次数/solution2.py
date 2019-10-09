class Solution(object):
    def getNumberOfK(self, nums, k):
        """
        :type nums: list[int]
        :type k: int
        :rtype: int
        """
        # 注意排序好的数组这个条件
        # 两个二分

        # 先往左
        low, high = 0, len(nums) - 1
        leftK = self.getleftK(nums, k, low, high)
        rightK = self.getrightK(nums, k, low, high)
        return rightK - leftK + 1
    def getleftK(self, nums, k, low, high):
        while low <= high: 
            mid = (low + high) // 2
            if nums[mid] >= k:
                high = mid - 1
            else: 
                low = mid + 1
        return low

    
    def getrightK(self, nums, k, low, high):
        while low <= high: 
            mid = (low + high) // 2
            if nums[mid] <= k:
                low = mid + 1
            else: 
                high = mid - 1
        return high

    






            

                
                