
from Treenode import TreeNode

class Solution(object):
    def buildTree(self, preorder, inorder):
        
        pos = {}
        for i in range(len(preorder)):
            pos[inorder[i]] = i   # {inorder[i] : i}

        return self.dfs(preorder, pos, 0, len(preorder) - 1, 0, len(preorder) - 1)

    def dfs(self, pre, pos, pl, pr, il, ir):
        # 减少inorder空间和查找操作
        if pl > pr:
            return None

        k = pos[pre[pl]] -  il  # 左子树size
        root = TreeNode(pre[pl])
        root.left = self.dfs(pre, pos,  pl + 1, pl + k, il, il + k)
        root.right = self.dfs(pre, pos, pl + k + 1, pr, il + k + 1, ir)
        
        return root
