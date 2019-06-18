
from Treenode import TreeNode

class Solution(object):
    def buildTree(self, preorder, inorder):
        '''
        preorder = list[int]
        inorder = list[int]
        return treenode
        递归法1
        '''
        
        if not preorder or not inorder: # 当某一子树无元素,输出None
            return None
            
        root = TreeNode(preorder.pop(0)  )
        idx = inorder.index(preorder.pop(0))   # 中序遍历找到根的位置

        # 构造
        root.left = self.buildTree(preorder, inorder[: idx])
        root.right = self.buildTree(preorder, inorder[idx + 1 :])

        return root

