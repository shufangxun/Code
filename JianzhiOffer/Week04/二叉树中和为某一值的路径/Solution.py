# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # 每个列表表示找到的路径
    def findPath(self, root, sum):
        res = []
        if not root:
            return []
        if not root.left and not root.right and sum == root.val:
            return [[root.val]]

        left = self.findPath(root.left, sum-root.val)
        right = self.findPath(root.right, sum-root.val)
        for subpath in left + right:
            res.append([root.val] + subpath)
        
        return res
            
