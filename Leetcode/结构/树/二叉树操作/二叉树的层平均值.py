# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels1(self, root: TreeNode) -> List[float]:
        if root is None: return None
        queue = [root]
        res = []
        while queue:
            curQ, nextQ = [], []
            for node in queue:
                curQ.append(node.val)
                if node.left: nextQ.append(node.left)
                if node.right: nextQ.append(node.right)
            res.append(float(sum(curQ)) / len(curQ))
            queue = nextQ
        return res

    def averageOfLevels2(self, root: TreeNode) -> List[float]:
        if root is None: return None
        queue = [root]
        res = []
        while queue:
            n = len(queue)
            sum = 0
            for i in range(n):
                node = queue.pop(0)
                sum += node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(sum/n)
        return res