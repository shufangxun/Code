class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class CycleLinklist:
    def __init__(self, node=None):
        # 初始化要头尾相连
        if node:
            node.next = node
        self.head = node

    def is_empty(self):
        return self.head is None

    def length(self):
        if self.is_empty():
            return 0
        
        p = self.head
        count = 1
        while p.next != self.head:
            p = p.next
            count += 1
        
        return count

    def traversal(self):
        elem = []
        if self.is_empty():
            print(elem)
            return

        p = self.head
        while p.next != self.head:
            elem.append(p.val)
            p = p.next
        elem.append(p.val)

        print(elem)

    def add(self, val):
        '''
            头插入
        '''
        node = Node(val)

        if self.is_empty():
            # 自己指向自己,并且定为head
            node.next = node
            self.head = node
        else:
            node.next = self.head

            p = self.head
            while p.next != self.head:
                p = p.next
            p.next = node 
            self.head = node


    def append(self, val):
        '''
            尾插入
        '''
        node = Node(val)

        if self.is_empty():
            # 自己指向自己,并且定为head
            node.next = node
            self.head = node
        else:
            p = self.head
            while p.next != self.head:
                p = p.next
            p.next = node 
            node.next = self.head


    def insert(self, pos, val):
        '''
            任意位置插入
        '''
        if pos <= 0:
            self.add(val)
        elif pos >= self.length():
            self.append(val)
        else:
            p = self.head
            while pos:
                pos -= 1
                p = p.next 
            node = Node(val)
            node.next = p.next
            p.next =node

    
    def remove(self, val):
        if self.is_empty():
            return
        
        p = self.head
        pre = None
        
        while p.next != self.head:
            # 第一次是分析删除节点是不是在头部
            if p.val == val:
                if p == self.head:
                    rear = self.head
                    while rear.next != self.head:
                        rear = rear.next
                    self.head = p.next
                    rear.next = self.head
                else:
                    pre.next = p.next
                return
            else:
                pre = p
                p = p.next

        if p.val == val:
            # 如果链表中只有一个元素，则此时prior为None，Next属性就会报错
            # 此时直接使其头部元素为None即可
            if p == self.head:
                self.head = None
                return
            pre.next = p.next

            

    def search(self, val):
        p = self.head

        while p.next != self.head:
            if p.val == val:
                return True
            p = p.next
        # 退出循环后, cur指向了尾节点
        if p.val == val:
            return True
        return False


if __name__ == '__main__':
    ll = CycleLinklist()
    print(ll.length())

    ll.append(1)   # 1
    print(ll.length())
    ll.traversal()

    ll.append(2)   #1 2
    print(ll.length())
    ll.traversal()

    ll.add(3)   # 3 1 2
    ll.traversal()

    ll.add(4) # 4 3 1 2
    ll.traversal()

    ll.insert(0, 5)  # 5 4 3 1 2
    ll.traversal()

    ll.insert(10, 6)  # 5 4 3 1 2  6
    ll.traversal()

    ll.insert(3, 7)  # 5 4 3  7 1 2  6
    ll.traversal()

    ll.remove(5)  #  4 3  7 1 2  6)
    ll.traversal()

    ll.remove(6)  #  4 3  7 1 2
    ll.traversal()

    ll.remove(7)  #  4 3  1 2
    ll.traversal()

    ll.remove(4)  #  3  1 2
    ll.traversal()
    ll.remove(3)  #   1 2
    ll.traversal()
    ll.remove(1)  #  2
    ll.traversal()
    ll.remove(2)
    ll.traversal()