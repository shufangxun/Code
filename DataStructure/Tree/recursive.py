class Node:  
    def __init__(self, value = None, left = None, right = None):           
        self.value = value  
        self.left = left    #左子树
        self.right = right   #右子树


    def preTraverse(self, root):
        if root is None:
            return 
        print(root.value)
        self.preTraverse(root.left)
        self.preTraverse(root.right)

    def midTraverse(self, root):
        if root is None:
            return 
        self.preTraverse(root.left)
        print(root.value)
        self.preTraverse(root.right)

    def postTraverse(self, root):
        if root is None:
            return 
        self.preTraverse(root.left)
        self.preTraverse(root.right)
        print(root.value)

if __name__=='__main__':
    root=Node('D',Node('B',Node('A'),Node('C')),Node('E',right=Node('G',Node('F'))))
    root.preTraverse(root)
    print('\n')
    root.midTraverse(root)
    print('\n')
    root.postTraverse(root)