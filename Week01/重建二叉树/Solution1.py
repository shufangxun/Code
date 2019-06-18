
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
class Solution(object):
    def buildTree(self, preorder, inorder):
        '''
        preorder = list[int]
        inorder = list[int]
        return treenode
        递归法
        '''
        
        if not preorder or not inorder: # 当某一子树无元素,输出None
            return None
            
        root = TreeNode(preorder.pop(0)  )
        idx = inorder.index(preorder.pop(0))   # 中序遍历找到根的位置

        # 构造
        root.left = self.buildTree(preorder, inorder[: idx])
        root.right = self.buildTree(preorder, inorder[idx + 1 :])

        return root

