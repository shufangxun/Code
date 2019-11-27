# 二叉树

## 遍历

### 前序遍历

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

### 中序遍历

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

### 后序遍历

>给定一个二叉树，返回它的后序遍历

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

### 层次遍历

> 给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）

思路：运用队列，每层先保存，然后再将下一层存储

```python
class Solution:
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
            res.append(curQ)
            queue = nextQ
        return res
```

### 从前序与中序遍历序列构造二叉树

>给出二叉树的前序和中序遍历, 重建二叉树

```txt
输入:  
前序遍历：[3, 9, 20, 15, 7]  
中序遍历：[9, 3, 15, 20, 7]  
返回：  
[3, 9, 20, null, null, 15, 7, null, null, null, null]
```

思路：
前序遍历的第一个结点是根结点，以此划分中序遍历，左边是左子树，右边是是右子树

```python
class Solution(object):
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1 : idx+1], inorder[ : idx])
        root.right = self.buildTree(preorder[idx + 1: ], inorder[idx + 1: ])

        return root
```

### 从中序与后序遍历序列构造二叉树

> 给出中序和后序遍历数组．重建二叉树  

```txt
中序遍历 inorder = [9,3,15,20,7]  
后序遍历 postorder = [9,15,7,20,3]
```

解法: 后序遍历的最后一个元素是根结点，以此划分中序遍历，右边是右子树，左边是左子树　　

```python
class Solution(object):
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None

        root = TreeNode(postorder[-1])
        idx = inorder.index(postorder[-1])

        root.left = self.buildTree(inorder[ : idx], postorder[: idx])
        root.right = self.buildTree(inorder[idx + 1 :], postorder[idx : -1])

        return root
```

## 二叉树的下一个节点

>给定一棵二叉树的其中一个节点，请找出中序遍历序列的下一个节点。

解法:
如果此结点有右子树，则遍历到最左结点；如果此结点没有右子树，则分类讨论

1) 此结点是其父节点的左结点，则直接返回父节点
2) 此节点是其父节点的右结点，则找到是其左结点的结点，返回父结点的父结点

```python
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

## 对称二叉树

>给定一个二叉树，检查它是否是镜像对称的.  

法1：递归法

- 怎么判断一棵树是不是对称二叉树  
  如果根节点为空，那么是对称。如果不为空，判断左右子树是否对称
- 如何判断左子树与右子树是否对称
  - 左子树根节点和右子树根节点相等  
  - 左子树的左孩子与右子树的右孩子对称，左子树的右孩子与右子树的左孩子对称，那么这个左子树和右子树就对称　　

```python
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None：
            return True
        return self.

    def check(self, node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        return node1.val == node2.val and self.check(node1.left, node2.right) and self.check(node1.right, node2.left)
```

法2：迭代法
层序遍历，判断每一层是否是回文数组

```python
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = [root]
        while queue:
            nexQ, curQ = list(), list()
            for node in queue:
                if not node:
                    curQ.append(None)
                    continue
                curQ.append(node.val)
                # 和层序遍历的区别
                nexQ.append(node.left)
                nexQ.append(node.right)
            # 判断是否是回文数组
            if curQ != curQ[::-1]:
                return False
            queue = nexQ
        return True
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

## 二叉树的最小深度

> 1、给定一个二叉树，找出其最小深度。  
> 2、最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

解法：递归，注意叶子节点的定义

- 叶子节点是没有左右孩子的节点

```python
def minDepth(root):
    if root is None:
        return 0
    l = minDepth(root.left)
    r = minDepth(root.right)
    if root.left is None or root.right is None:
        return l + r + 1
    return min(l, r) + 1
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

## 合并二叉树

> 合并两个二叉树，重合结点对应值相加，不重合直接作为新树结点

解法：递归

- 递归判断对应左右结点是否存在
- 存在则相加
- 不存在返回另一边
  
```python
def mergeTrees(t1, t2):
    if t1 is None:
        return t2
    if t2 is None:
        return t1
    if not t1 and not t2:
        return None
    if t1 and t2:
        t1.val += t2.val
        t1.left = mergeTrees(t1.left, t2.left)
        t1.right = mergeTrees(t1.right, t2.right)
        return t1
```

## 字典树

题目要求

```python
Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   # 返回 true
trie.search("app");     # 返回 false
trie.startsWith("app"); # 返回 true
trie.insert("app");
trie.search("app");     # 返回 true
```

实现代码

```python
class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.Trie = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur = self.Trie
        for w in word:
            # 加入到字典
            if w not in cur:
                cur[w] = {}
            # 移动到下一个字符
            cur = cur[w]
        cur['#'] = 1

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.Trie
        for w in word:
            if w not in cur.keys():
                return False
            cur = cur[w]
        return True if '#' in cur else False

    def startWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.Trie
        for w in prefix:
            if w not in cur.keys():
                return False
            cur = cur[w]
        return True
```
