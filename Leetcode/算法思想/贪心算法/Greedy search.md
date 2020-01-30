# 贪心算法

## 数组中两个数的最大异或值

见位运算

## 数组中两个数相加最大值

贪心算法

- 左右两个指针i，j
- 先更新最大和
- 然后更新左边元素nums[i]为更大的nums[j]
- 时间复杂度: $O(n)$

```python
def maxadd(nums):
    if len(nums) == 0:
        return None
    elif len(nums) == 1:
        maxSum = nums[0]
    else:
        maxSum = nums[0] + nums[1]
    i = 0
    for j in range(1, len(nums)):
        curSum = nums[i] + nums[j]
        if curSum > maxSum:
            maxSum = curSum
        if nums[i] < nums[j]:
            i = j
    return maxSum
```

## 判断子序列

> 给定字符串 s 和 t ，判断 s 是否为 t 的子序列

```bash
s = "abc", t = "ahbgdc"

return true
```

贪心规则

从头遍历子字符串:

- 当字符 'a' 出现，判断字符串 t 中是否存在字符 'a'
- t 中字符 'a' 之后的剩余字符串是否存在 'b'

写法和双指针法一样
