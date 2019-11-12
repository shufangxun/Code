class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        return self.dfs(root.left, root.right)

    def dfs(self, l, r):
        if not l or not r:
            return not l and not r

        return l.val == r.val and self.dfs(l.left, r.right) and self.dfs(l.right, r.left)