# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.father = None
class Solution(object):
    def inorderSuccessor(self, q):
        """
        :type q: TreeNode
        :rtype: TreeNode
        """
        if q.right: 
            q = q.right
            while q.left:
                q = q.left
            return q
        
        while q.father and q.father.right == q:
            q = q.father
        return q.father 