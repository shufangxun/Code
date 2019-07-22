# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.Balanced = True
        self.height(root)
        return self.Balanced
    

    def height(self, root):
        if root is None:
            return 0
        
        l = self.height(root.left)
        r = self.height(root.right)
        if abs(l - r) > 1:
            self.Balanced = False
        return max(l, r) + 1