# 无序数组
def twoSum1(nums, K):
    d = dict()
    for i in range(len(nums)):
        tmp = K - nums[i]
        if tmp in d:
            return [i, d[tmp]]
        d[nums[i]] = i
    return None

# 有序数组
def twoSum2(self, numbers, target):
    i, j = 0, len(numbers) - 1
    while i < j:
        curSum = numbers[i] + numbers[j]
        if curSum == target:
            return [i+1, j+1]
        elif curSum < target:
            i += 1
        else:
            j -= 1

# 和小于K的两数之和
def twoSumLessThanK(self, A: List[int], K: int) -> int:
    A.sort()
    maxSum = -1
    i, j = 0, len(A) - 1
    while i < j:
        curSum = A[i] + A[j]
        if curSum < K:
            i += 1
            maxSum = max(maxSum, curSum)
        else:
            j -= 1
    return maxSum