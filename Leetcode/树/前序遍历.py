# 迭代
def preorderTraversal1(root):
        if root is None: return []
        stack = [root]
        ans = []
        while stack:
            tmp = stack.pop()
            ans.append(tmp.val)
            if tmp.right:
                stack.append(tmp.right)
            if tmp.left:
                stack.append(tmp.left)
        return ans

# 递归
def preTraversal2(root):
        if root is None:
            return []
        return [root.val] + preTraversal(root.left) + preTraversal(root.right)