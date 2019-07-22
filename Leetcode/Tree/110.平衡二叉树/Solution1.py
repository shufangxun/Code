# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        l = self.h(root.left)
        r = self.h(root.right)
        
        if abs(l - r) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def h(self, root):
        if root is None:
            return 0
        return max(self.h(root.left), self.h(root.right)) + 1
        