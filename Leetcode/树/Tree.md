# 二叉树

## 前序遍历

> 给定一个二叉树，写出前序遍历数组

解法1：递归

```python
class Solution:
    def preTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        return [root.val] + self.preTraversal(root.left) + self.preTraversal(root.right)
```

解法2：迭代

- 遍历先保存当前结点
- 右边先入栈，左边后入栈

```python
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
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
```

## 中序遍历

> 给定一棵二叉树，写出中序遍历数组

解法1：递归，用__init__(self)构造一个全局变量

```python
class Solution:
    def __init__(self):
        self.ans = []
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return
        self.inorderTraversal(root.left)
        self.ans.append(root.val)
        self.inorderTraversal(root.right)
        return self.ans
```

解法2：递归，避免定义__init__函数

```python
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
```

解法3： 用栈存储遍历，遍历到最左边后，再迭代弹出

```python
class Solution:
   def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans, stack = [], []
        if root is None: return []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                tmp = stack.pop()
                ans.append(tmp.val)
                root = tmp.right
        return ans
```

## 后序遍历

>给定一个二叉树，返回它的 后序 遍历

解法1：递归

```python
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
```

解法2：迭代

- 先写出后序遍历的数组
- 然后分析如何利用栈弹出，可知从右边往左弹
- 构建两个栈来维护

```python
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None: return []
        stack1 = [root]
        stack2 = []
        while stack1:
            tmp = stack1.pop()
            stack2.append(tmp.val)
            if tmp.left: stack1.append(tmp.left)
            if tmp.right: stack1.append(tmp.right)
        return stack2[::-1]

```

## 二叉树的下一个节点

>给定一棵二叉树的其中一个节点，请找出中序遍历序列的下一个节点。

解法:
如果此结点有右子树，则遍历到最左结点；如果此结点没有右子树，则分类讨论

1) 此结点是其父节点的左结点，则直接返回父节点
2) 此节点是其父节点的右结点，则找到是其左结点的结点，返回父结点的父结点

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.father = None
class Solution(object):
    def inorderSuccessor(self, q):
        if q.right:
            q = q.right
            while q.left:
                q = q.left
            return q
        else:
            if q.father.left = q:
                return q.father
            else:
                while q.father and q.father.right == q:
                    q = q.father
                return q.father
```

## 从前序与中序遍历序列构造二叉树

>给出二叉树的前序和中序遍历, 重建二叉树:  
>输入:  
前序遍历：[3, 9, 20, 15, 7]  
中序遍历：[9, 3, 15, 20, 7]  
返回：  
[3, 9, 20, null, null, 15, 7, null, null, null, null]

解法:
前序遍历的第一个结点是根结点，以此划分中序遍历，左边是左子树，右边是是右子树

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1 : idx+1], inorder[ : idx])
        root.right = self.buildTree(preorder[idx + 1: ], inorder[idx + 1: ])

        return root
```

## 从中序与后序遍历序列构造二叉树

> 给出中序和后序遍历数组．重建二叉树  
> 中序遍历 inorder = [9,3,15,20,7]  
后序遍历 postorder = [9,15,7,20,3]

解法: 后序遍历的最后一个元素是根结点，以此划分中序遍历，右边是右子树，左边是左子树　　

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder:
            return None

        root = TreeNode(postorder[-1])
        idx = inorder.index(postorder[-1])

        root.left = self.buildTree(inorder[ : idx], postorder[: idx])
        root.right = self.buildTree(inorder[idx + 1 :], postorder[idx : -1])

        return root
```

## 对称二叉树

>给定一个二叉树，检查它是否是镜像对称的.  
例如，二叉树 [1,2,2,3,4,4,3] 是对称的.

解法：递归  
基：当根结点为空时，返回True；当左右子树为空时：1) 左空右不空(或者右空左不空，返回False)；2) 左右都空，返回True  
递归：左子树的左＝右子树的右 and 右子树的左＝左子树的右 and 左根＝右根　　

```python
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
```

## 镜像二叉树
>输入一个树，讲其变为自身镜像

解法：前序遍历，变换左右结点，交换完之后**下面子树**连带交换

```python
class Solution(object):
    def mirror(self, root):
        """
        :type root: TreeNode
        :rtype: void
        """
        if root is None:
            return None
        root.left, root.right = root.right, root.left
        self.mirror(root.left)
        self.mirror(root.right)
```

## 二叉树的最大深度

> 给定一个二叉树，求最大深度

解法：递归求左右子树的最大深度

```python
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        return max(l, r) + 1
```

## 平衡二叉树

> 如果某二叉树中任意结点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。

解法：

```python
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        # 左右子树深度
        l = self.height(root.left)
        r = self.height(root.right)
        if abs(l-r) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    def height(self, root):
        if root is None:
            return 0
        l = self.height(root.left)
        r = self.height(root.right)
        return max(l, r) + 1
```
