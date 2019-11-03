# 不打印序列
def LIS1(nums):
    if len(nums) <= 1:
        return len(nums)
    else:
        dp = [1] * len(nums)
        # 两层循环
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1) # 关键
    return max(dp)

# 打印序列
def LIS1print(nums):
    if len(nums) <= 1:
        return len(nums)
    else:
        dp = [1] * len(nums)
        # 两层循环
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1) # 关键
    
    maxlen = max(dp)

    # 返回子序列
    subS = []
    for i in range(len(nums)-1, -1, -1):
        if dp[i] == maxlen:
            subS.append(nums[i])
            maxlen -= 1
    subS.reverse() # 取反
    return subS 
    


def LIS2(nums):
    if len(nums) <= 1:
        return len(nums)
    # 维护一个队列
    queue = []
    queue.append(nums[0])
    for i in range(1, len(nums)):
        if nums[i] > queue[-1]:
            queue.append(nums[i])
        else:
            l, r = 0, len(queue) - 1
            while l < r:
                # 二分搜索
                mid = l + (r - l) // 2
                if queue[mid] < nums[i]:
                    l = mid + 1
                else:
                    r = mid
            queue[l] = nums[i]  # 关键替换
    return len(queue)

# 打印长度和序列值

if __name__ == "__main__":
    a = [1,6,3,4,7,8,2,4,9,1,19,9,9]
    print(LIS1(a))
    print(LIS2(a))
    print(LIS1print(a))


