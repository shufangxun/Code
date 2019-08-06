# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def treeDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        lDepth = self.treeDepth(root.left)
        rDepth = self.treeDepth(root.right)
        return max(lDepth, rDepth) + 1