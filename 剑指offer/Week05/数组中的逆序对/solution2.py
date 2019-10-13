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

        self.mergesort(nums)
        return self.count

    def mergesort(self, nums):
        if len(nums) < 2:
            return nums
        
        mid = len(nums) // 2
        # 左右都已归并排序计数好
        left = self.mergesort(nums[:mid])
        right = self.mergesort(nums[mid:])

        # 计数左右之间
        i, j = 0, 0 
        sorted = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                sorted.append(left[i])
                i += 1
            else:
                sorted.append(right[j])
                j += 1
                self.count += (len(left)-i)

        return sorted + left[i:] + right[j:]
    