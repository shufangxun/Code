from Iterative import reverse1
from Recursive import reverse2
from NodeClass import Node

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

# 迭代反转
s1 = reverse1(head)
while s1:
    print(s1.element)
    s1 = s1.next 

# 递归反转
s2 = reverse2(head)
while s2:
    print(s2.element)
    s2 = s2.next 