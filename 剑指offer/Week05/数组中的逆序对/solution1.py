class Solution(object):
    def __init__(self):
        self.count = 0

    def inversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        tmp = [0] * len(nums)
        self.mergecount(nums, tmp, 0, len(nums) - 1)
        return self.count 

    ## 排序+计数
    def mergecount(self, nums, tmp, left, right):
        if left >= right:
            return 
        mid = left + (right - left) // 2
        self.mergecount(nums, tmp, left, mid)
        self.mergecount(nums, tmp, mid+1, right)
        i, j, k = left, mid+1, 0
        while i <= mid and j <= right:
            if nums[i] < nums[j]:
                tmp[k] = nums[i]
                i += 1
                k += 1
            else:
                self.count += mid - i + 1 # 计数部分
                tmp[k] = nums[j]
                j += 1
                k += 1

        while i <= mid:
            tmp[k] = nums[i]
            k += 1
            i += 1
        while j <= right:
            tmp[k]=nums[j]
            k += 1
            j += 1
        
        m = 0
        while left <= right: 
            nums[left] = tmp[m]
            m += 1
            left += 1

        



           
        