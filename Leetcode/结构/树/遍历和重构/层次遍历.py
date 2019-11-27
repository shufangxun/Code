# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if root is None:
            return res
        queue = [root]
        while queue:
            curQ, nextQ = list(), list()
            for node in queue:
                curQ.append(node.val)
                if node.left:
                    nextQ.append(node.left)
                if node.right:
                    nextQ.append(node.right)
            res.append(curQ)
            queue = nextQ
        return res
