# 双指针

## 合并两个有序数组

> 给定两个有序整数数组 $nums1$ 和 $nums2$，将 nums2 合并到 $nums1$ 中，使得 $num1$ 成为一个有序数组  
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
