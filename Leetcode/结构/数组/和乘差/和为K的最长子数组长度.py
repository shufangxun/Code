class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        sum, length = 0, 0
        prefix = {0 : -1}
        for i in range(len(nums)):
            sum += nums[i]
            if sum not in prefix:
                prefix[sum] = i
            if sum - k in prefix:
                length = max(length, i - prefix[sum - k])
        return length