# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def printFromTopToBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 开辟两个空间
        if root is None:
            return []
        q = [root]
        res = []

        while q:
            curQ, nexQ = [], []
            for node in q: # 不用pop
                curQ.append(node.val)
                if node.left:
                    nexQ.append(node.left)
                if node.right:
                    nexQ.append(node.right)
            res.append(curQ)
            q = nexQ
        return res

