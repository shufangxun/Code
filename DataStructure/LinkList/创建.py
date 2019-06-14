class Node:
    def __init__(self,element):
        self.element = element
        self.next = None


def reverse(head):
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev
    
if __name__ == "__main__":

    # 创建节点
    node1 = Node(10)
    node2 = Node(9)
    node3 = Node(8)
    node4 = Node(3)

    # 连接链表
    head = node1
    head.next = node2
    node2.next = node3
    node3.next = node4


    s = reverse(head)
    while s:
        print(s.element)
        s = s.next 
    