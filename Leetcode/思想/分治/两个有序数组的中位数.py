class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1, l2 = len(nums1), len(nums2)
        left, right = (l1 + l2 + 1) // 2, (l1 + l2 + 2) // 2
        return (self.findKthElement(nums1, nums2, left) + self.findKthElement(nums1, nums2, right)) / 2
    
    def findKthElement(self, nums1, nums2, k):
        l1, l2 = len(nums1), len(nums2)
        if l1 > l2:
            return self.findKthElement(nums2, nums1, k)
        if not nums1:
            return nums2[k - 1]
        if k == 1:
            return min(nums1[0], nums2[0])
        i, j = min(k // 2, l1) - 1, min(k // 2, l2) - 1
        if nums1[i] > nums2[j]:
            return self.findKthElement(nums1, nums2[j + 1: ], k - j - 1)
        else:
            return self.findKthElement(nums1[i + 1: ], nums2, k - i - 1)