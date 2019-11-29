# 双指针

## 合并两个有序数组

> 给定两个有序整数数组 $nums1$ 和 $nums2$，将 $nums2$ 合并到 $nums1$ 中，使得 $num1$ 成为一个有序数组  
> 1.初始化 $nums1$ 和 $nums2$ 的元素数量分别为 m 和 n  
> 2.你可以假设 $nums1$ 有足够的空间（空间大小大于或等于 $m + n$）来保存 $nums2$ 中的元素  

- 从尾到头遍历 空间复杂度$O(1)$

```python
def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i, j = m - 1, n - 1
    for k in range(m + n - 1, -1, -1):
        if i == -1:
            nums1[k] = nums2[j]
            j -= 1
        elif j == -1:
            break
        elif nums1[i] < nums2[j]:
            nums1[k] = nums2[j]
            j -= 1
        else:
            nums1[k] = nums1[i]
            i -= 1

```

## 判断子序列

> 给定字符串 s 和 t ，判断 s 是否为 t 的子序列

```python
def isSubsequence1(s, t):
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            j += 1
    return False if i < len(s) else True
```

## 两数之和系列

### 无序数组两数之和

> 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标

思路: 哈希表

- 时间复杂度：$O(n)$
- 空间复杂度：$O(n)$

```python
def twoSum(nums, K):
    d = dict()
    for i in range(len(nums)):
        tmp = K - nums[i]
        if tmp in d:
            return [i, d[tmp]]
        d[nums[i]] = i
    return None
```

### 有序数组两数之和

思路:双指针分别指向头和尾

```python
def twoSum(self, numbers, target):
    i, j = 0, len(numbers) - 1
    while i < j:
        curSum = numbers[i] + numbers[j]
        if curSum == target:
            return [i+1, j+1]
        elif curSum < target:
            i += 1
        else:
            j -= 1
```

### 小于K的两数之和

> 给你一个整数数组 A 和一个整数 K，请在该数组中找出两个元素，使它们的和小于 K 但尽可能地接近 K，返回这两个元素的和

思路: 排序加双指针

```python
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
```
