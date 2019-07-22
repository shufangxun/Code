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
        if root is None:
            return True
        l = self.height(root.left)
        r = self.height(root.right)
        
        # 每一次递归都要判断
        if abs(l - r) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right) 
        
    
    # 求高度
    def height(self, root):
        if root is None:
            return 0
        l = self.height(root.left)
        r = self.height(root.right)
        return max(l, r) + 1