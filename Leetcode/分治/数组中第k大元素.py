from random import randint
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k > len(nums):
            return
        index = randint(0,len(nums)-1)
        pivot = nums[index]
        less_part = [i for i in nums[:index]+nums[index+1:] if i < pivot]
        great_part = [i for i in nums[:index]+nums[index+1:] if i >= pivot]
        if len(great_part) == k-1:
            return pivot
        elif len(great_part) > k-1:
            return self.findKthLargest(great_part,k)
        else:
            return self.findKthLargest(less_part,k-len(great_part)-1)
