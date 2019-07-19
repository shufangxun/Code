# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def KthNode(self, root, k):
        # 中序遍历二叉树
        # 栈模拟
        if not root or k <= 0:
            return None
        stack = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            k -= 1
            if k == 0:
                return node
            node = node.right
        if k > 0:
            return None
