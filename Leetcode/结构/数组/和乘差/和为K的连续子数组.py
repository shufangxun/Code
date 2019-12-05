class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {0:1}
        sum, count = 0, 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum - k in hashmap:
                count += hashmap[sum - k]
            if sum in hashmap:
                hashmap[sum] += 1
            else:
                hashmap[sum] = 1
        return count