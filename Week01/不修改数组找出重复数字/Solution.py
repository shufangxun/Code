class Solution(object):
    def duplicateInArray(self, nums):
        """
        :type nums: List[int]
        :rtype int
        """
        if nums == [] or max(nums) > len(nums) - 1:
            return -1

        # 取值范围
        start = 1
        end = len(nums) - 1

        while start < end:
            mid = (start + end) >> 1 # 取值范围划分为[start, mid], [mid+1, end]

            count = 0 
            for num in nums:
                if num >= start and num <= mid: # 统计半边
                    count += 1

            if count > mid - start + 1:
                end = mid
            else:
                start = mid + 1

        return end  # 当 start = end 结束查找
