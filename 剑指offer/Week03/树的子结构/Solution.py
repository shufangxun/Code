# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasSubtree(self, pRoot1, pRoot2):
        """
        :type pRoot1: TreeNode
        :type pRoot2: TreeNode
        :rtype: bool
        """
        # 空树不匹配
        if pRoot1 is None or pRoot2 is None:
            return False
        if self.isSame(pRoot1, pRoot2):
            return True

        return self.hasSubtree(pRoot1.left, pRoot2) or self.hasSubtree(pRoot1.right, pRoot2)

    def isSame(self, p1, p2):
        if p2 is None: # 说明B到达叶子节点，遍历结束
            return True
        if p1 is None:
            return False # 说明A到达叶子节点，未找到相同
        if p2.val != p1.val: # 对应跟节点就不相等
            return False
        
        return self.isSame(p1.right, p2.right) and self.isSame(p1.left, p2.left) # 左右子树都一样，重点是遍历完B树

        

        