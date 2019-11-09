def sumofsubS(nums):
    sum = 0
    ans = nums[0]
    for i in range(len(nums)):
        if sum > 0:
            sum += nums[i]
        else:
            sum = nums[i]
        ans = max(sum, ans)
    return ans