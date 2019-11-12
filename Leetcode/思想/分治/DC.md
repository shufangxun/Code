# 分治

## 数组中第 $k$ 大的元素

> 返回无序数组中第 $k$ 大的元素，已有的一种解法是维护一个最小堆，时间复杂度$O(Nlogk)$，空间复杂度$O(k)$

新解法：基于快速排序思想，时间复杂度降低到$O(n)$，空间复杂度$O(1)$

- 先随机选取一个元素 $a$，获取其索引
- 然后用快排思想得到小于和大于 $a$ 的左右子序列
- 判断左序列是否长度是否 大于 $n-k$
  - 若大于 $n-k$，第 $k$ 大元素在左子序
  - 若小于，在右子序
  - 若等于，输出

```python
from random import randint
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k > len(nums):
            return
        index = randint(0,len(nums)-1)
        pivot = nums[index]
        less_part = [i for i in nums[:index]+nums[index+1:] if i < pivot]
        great_part = [i for i in nums[:index]+nums[index+1:] if i >= pivot]
        if len(great_part) == k-1:
            return pivot
        elif len(great_part) > k-1:
            return self.findKthLargest(great_part,k)
        else:
            return self.findKthLargest(less_part,k-len(great_part)-1)
```
