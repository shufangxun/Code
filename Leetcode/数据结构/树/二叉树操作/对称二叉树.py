# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 递归法
class Solution1(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None：
            return True
        return self.

    def check(self, node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        return node1.val == node2.val and self.check(node1.left, node2.right) and self.check(node1.right, node2.left)

# 迭代法
class Solution2(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = [root]
        while queue:
            nexQ, curQ = list(), list()
            for node in queue:
                if not node:
                    curQ.append(None)
                    continue
                curQ.append(node.val)
                # 和层序遍历的区别
                nexQ.append(node.left)
                nexQ.append(node.right)
            # 判断是否是回文数组
            if curQ != curQ[::-1]:
                return False
            queue = nexQ
        return True