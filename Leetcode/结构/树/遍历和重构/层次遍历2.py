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
            res.insert(0, curQ)
            queue = nextQ
        return res