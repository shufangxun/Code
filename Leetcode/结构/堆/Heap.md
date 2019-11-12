# 堆总结

## 数组中第k大的元素

> 在未排序的数组中找到第k个最大的元素。请注意，你需要找的是数组排序后的第k个最大的元素，而不是第 k 个不同的元素

变形：  
1、10亿数中，找出最大的100个数。用能想到的最优的时间和空间效率。  
2、时间空间复杂度是多少？如何计算?

解法：

- 取无序序列的前k个元素，维护一个大小为k的最小堆
- 然后遍历剩余元素，与堆顶比较
  - 如果比堆顶小，不加入堆
  - 如果比堆顶大，替换堆顶元素，并维护堆的性质
- 遍历完堆顶元素就是第K大元素
- 时间复杂度 $O(nlogk)$
  - 构建堆 $O(k)$
  - 维护堆 $O(nlogk)$
- 空间复杂度 $O(k)$

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        self.build_heap(heap)
        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heap[0] = nums[i]
                self.shiftdown(heap, 0)
        return heap[0]  # 堆顶就是第k大元素
    # 自底向上构建堆
    def build_heap(self, A):
        n = len(A)
        for i in range(n // 2 - 1, -1, -1):
            self.shiftdown(A, i)
    # 维护堆的性质，下沉
    def shiftdown(self, A, i):
        small_child = -1
        while 2 * i <= len(A) - 1:
            l = 2 * i + 1
            r = 2 * i + 2
            if l <= len(A) - 1:
                small_child = l
            if r <= len(A) - 1 and A[r] < A[l]:
                small_child = r
            if A[i] > A[small_child]:
                A[i], A[small_child] = A[small_child], A[i]
                i = small_child
            else:
                break
```