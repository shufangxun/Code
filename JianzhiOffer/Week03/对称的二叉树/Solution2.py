# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        
        l = root.left
        r = root.right

        stack_l = []
        stack_r = []

        while l or r or len(stack_l):
            while l and r:
                stack_l.append(l)
                stack_r.append(r)
                l = l.left
                r = r.right
            
            if l or r:
                return False # 说明左右子树深度不一样
            
            l = stack_l.pop()
            r = stack_r.pop()

            if l.val != r.val:
                return False
            
            l = l.right
            r = r.left
        
        return True
            


