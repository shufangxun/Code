class Node:
    def __init__(self,element):
        self.element = element
        self.next = None
    
if __name__ == "__main__":

    # 创建节点
    node1 = Node(10)
    node2 = Node(9)
    node3 = Node(8)
    node4 = Node(3)

    # 连接成链表
    head = node1
    head.next = node2
    node2.next = node3
    node3.next = node4

    while head:
        print(head.element)
        head = head.next 

    