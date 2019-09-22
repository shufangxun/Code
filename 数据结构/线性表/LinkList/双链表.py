class Node:
    def __init__(self, element = None):
        self.element = element
        self.next = None
        self.pre = None

'''
大部分不涉及节点变化的都一样:is_empty, __len__, traverse, search等
增删节点和定义节点时不同
'''
class DLinkList:
    def __init__(self):
        self.head = Node()
        self.size = 0
    

    # 判断链表是否为空
    def is_empty(self):
        return self.size == 0
    

    # 统计链表长度
    def get_length(self):
        return self.size


    # 遍历链表
    def traverse(self):
        elem  = []

        while self.head.next != None:
            self.head = self.head.next
            elem.append(self.head.element)
        
        print(elem)

    # 反转遍历链表
    def reverse(self):
        elem = []

        p = self.head.next
        while p != None:
            elem.insert(0, p.element)
            p = p.next

        print(elem)

    # 尾插入
    def append(self, data):
        new_node = Node(data)

        p = self.head
        while p.next != None:
            p = p.next
        
        p.next = new_node  # 先断开
        new_node.pre = p
     

    # 头插入
    def add(self, data):
        new_node = Node(data)

        # 后半截
        new_node.next = self.head.next
        self.head.next.pre = new_node
        # 前半截
        new_node.pre = self.head
        self.head.next = new_node


    # 插入第idx个节点
    def insert(self, data, idx):
        new_node = Node(data)

        if idx == 0:
            raise Exception('can not insert,as 0 index is head') # 第0个是头节点
        else:
            p = self.head
            while idx - 1:
                p = p.next
                if p == None:
                    raise Exception('out of range')
                idx -= 1
            
            new_node.next = p.next
            p.next.pre = Node

            new_node.pre = p
            p.next = new_node
    
    def reverse1(self):
        pre = None
        cur = self.head
        while cur:
            nex = cur.next
            cur.next = cur.pre
            cur.pre = nex

            pre = cur
            cur = nex
        return pre

if __name__ == "__main__":
    l = DLinkList()
    l.append(10)
    l.add(11)
    l.add(13)
    l.insert(112,2)
    l.append(1)
    l.reverse1()
    l.traverse()
    
