# 基于最小堆
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        self.build_heap(heap)
        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heap[0] = nums[i]
                self.shiftdown(heap, 0)
        return heap[0]
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

            
        