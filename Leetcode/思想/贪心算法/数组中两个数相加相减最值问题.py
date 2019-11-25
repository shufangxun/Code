
'''
求数组nums两个数相加的最大值
'''

# 双指针法
def maxadd1(nums):
    # 初始化maxSum
    if len(nums) == 0:
        return None
    if len(nums) == 1:
        maxSum = nums[0]
    else:
        maxSum = nums[0] + nums[1]
    # 先计算maxsum
    # 贪心更新左边的值
    i = 0
    for j in range(1, len(nums)):
        curSum = nums[i] + nums[j]
        if curSum > maxSum:
            maxSum = curSum
        if nums[j] > nums[i]:
            i = j
    return maxSum

def maxsub(nums):
    if len(nums) == 0:
        return None
    if len(nums) == 1:
        maxSub = nums[0]
    else:
        maxSub = nums[0] - nums[1]
    i = 0
    for j in range(1, len(nums)):
        curSub = nums[i] - nums[j]
        if curSub > maxSub:
            maxSub = curSub
        if nums[j] > nums[i]:
            i = j
    return maxSub

if __name__ == "__main__":
    nums = [1,-1,-2]
    print(maxsub(nums))



