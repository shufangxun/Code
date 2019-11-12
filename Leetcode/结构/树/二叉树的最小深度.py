# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        if root.left is None or root.right is None:
            return l + r + 1
        return min(l, r) + 1 