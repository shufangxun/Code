# 路径之和 I
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        elif root.left is None and root.right is None:
            return root.val == sum
        else:
            return self.hasPathSum(root.right, sum - root.val) or self.hasPathSum(root.left, sum - root.val)

# 路径总和 II
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        self.DFS(root, sum, [], res)
        return res

    def DFS(self, root, sum, path, res):
        if root is None:
            return
        path.append(root.val)
        if root.left is None and root.right is None and root.val == sum:
            # 不能用path 因为是引用
            res.append(path[:])
        else:
            self.DFS(root.left, sum-root.val, path, res)
            self.DFS(root.right, sum-root.val, path, res)
        # 回溯
        path.pop()