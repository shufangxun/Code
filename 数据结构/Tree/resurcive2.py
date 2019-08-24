class Node:  
    def __init__(self, value = None, left = None, right = None):           
        self.value = value  
        self.left = left    #左子树
        self.right = right   #右子树

    ## 用栈实现二叉树的遍历
    # 先序: 一直遍历左子树,遍历过程中打印节点
    def preTraverse(self, root):
        if root is None:
            return 

        stack = []
        node = root

        while stack or node:
            while node:
                print(node.value)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        
    # 中序: 一直遍历左子树,遍历完打印节点
    def midTraverse(self, root):
        if root is None:
            return 
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()  # 等于说访问了两次
            print(node.value)
            node = node.right

    def postTraverse(self, root):
        if root == None:
            return
        stack1 = []
        stack2 = []
        node = root
        stack1.append(node)
        while stack1:                   #这个while循环的功能是找出后序遍历的逆序，存stack2里面
            node = stack1.pop()
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
            stack2.append(node)
        while stack2:                         #将stack2中的元素出栈，即为后序遍历次序
            print(stack2.pop().value)



    def BFS(self, root):
        if root is None:
            return 
        queue = []
        queue.append(root)

        while queue:
            node = queue.pop(0)  # 把第0位取出来
            print(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)



if __name__=='__main__':
    root=Node('D',Node('B',Node('A'),Node('C')),Node('E',right=Node('G',Node('F'))))
    root.preTraverse(root)
    print('\n')
    root.midTraverse(root)
    print('\n')
    root.postTraverse(root)
    print('\n')
    root.BFS(root)




## 参考:https://blog.csdn.net/u014204761/article/details/82286730