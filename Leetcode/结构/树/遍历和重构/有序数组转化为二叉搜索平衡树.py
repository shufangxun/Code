# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if nums is None:
            return None
        return self.isTree(nums, 0, len(nums)-1)

    def isTree(self, nums, l, r):
        if l > r:
            return None
        m = (l + r) // 2
        root = TreeNode(nums[m])
        root.left = self.isTree(nums, l, m-1)
        root.right = self.isTree(nums, m+1, r)
        return root