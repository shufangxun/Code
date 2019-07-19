# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    count = 0
    def kthNode(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: TreeNode
        """
        if not root:
            return None
        
        # 遍历左子树
        node = self.kthNode(root.left, k)
        if node:
            return node
            
        self.count += 1

        # 根节点
        if self.count == k:
            return root
        
        # 遍历右子树
        node = self.kthNode(root.right, k)
        if node:
            return node

        