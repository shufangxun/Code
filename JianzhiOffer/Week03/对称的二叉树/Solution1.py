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
        # 递归法
        if root is None: # 当为空时,显然为对称树
            return True 
        return self.dfs(root.left, root.right)


    def dfs(self, l, r):
        if l is None or r is None:
            # l为空, r不为空, 返回False
            # l不为空, r为空, 返回False
            # l和r都为空,返回False
            return not l and not r 
        
        return l.val == r.val and self.dfs(l.left, r.right) and self.dfs(l.right, r.left)
