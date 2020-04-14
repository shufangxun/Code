class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        if not nums or n < 3: return ans

        nums.sort() # 升序排序

        for i in range(n):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue

            L, R = i + 1, n - 1
            while L < R:
                if nums[i] + nums[L] + nums[R] == 0:
                    ans.append([nums[i],nums[L],nums[R]])
                    while(L<R and nums[L]==nums[L+1]): L += 1
                    while(L<R and nums[R]==nums[R-1]): R -= 1
                    L += 1
                    R -= 1
                elif nums[i] + nums[L] + nums[R] < 0:
                    L += 1
                else:
                    R -= 1
        return ans
