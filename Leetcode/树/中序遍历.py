def inorderTraversal( root):
    if root is None:
        return []
    ans += inorderTraversal(root.left)
    ans.append(root.val)
    ans += inorderTraversal(root.rights)
    return ans
    '''
    if root is None:
        return []
    return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)
    '''

# 迭代
def inorderTraversal(root):
    ans = []
    stack = []
    if root is None:
        return []
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            tmp = stack.pop()
            ans.append(tmp.val)
            root = tmp.right
    return ans

# 递归
class Solution1:
    def __init__(self):
        self.ans = []
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return
        self.inorderTraversal(root.left)
        self.ans.append(root.val)
        self.inorderTraversal(root.right)
        return self.ans

