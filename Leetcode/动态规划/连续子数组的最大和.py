def sumofsubS(nums):
    if nums is None:
        return None
    elif len(nums) == 1:
        return nums[0]
    else:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if dp[i - 1] > 0:
                dp[i] = dp[i - 1] + nums[i]
            else:
                dp[i] = nums[i]
        return max(dp)