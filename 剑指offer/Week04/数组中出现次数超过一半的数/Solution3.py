class Solution(object):
    def moreThanHalfNum_Solution(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = len(nums)
        low = 0
        high = L - 1
        mid = (low + high) // 2  ## 不管数目是奇偶，向下取整 
        
        ## 异常处理：当数组为空时
        if L == 0:
            return 0
            
        index = self.Partition(nums, low, high)
        while(index != mid):
            if index > mid:
                high = index - 1
                index = self.Partition(nums, low, high)
            else:
                low = index + 1
                index = self.Partition(nums, low, high)
            
        res = nums[index]
        count = 0
        for i in range(L):
            if nums[i] == res:
                count += 1
        
        return res if count*2 > L else 0

    def Partition(self, nums, front, rear):
        pivot = nums[front]
        while front < rear:
            while front < rear and nums[rear] >= pivot: # 为什么这里重复front < rear
                rear -= 1
            # nums[front] = nums[rear]
            while front < rear and nums[front] < pivot:
                front += 1
            # nums[rear] = nums[front]
            nums[rear], nums[front] = nums[front], nums[rear]
        nums[front] = pivot
        return front
