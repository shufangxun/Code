# 迭代写法
def postorderTraversal1(root):
    if root is None: return []
    stack1 = [root]
    stack2 = []
    while stack1:
        tmp = stack1.pop()
        stack2.append(tmp.val)
        if tmp.left: stack1.append(tmp.left)
        if tmp.right: stack1.append(tmp.right)
    return stack2[::-1]

# 递归写法
def postorderTraversal2(root):
    if root is None: return []
    return postorderTraversal(root.left) + postorderTraversal(root.right) + [root.val]