
## 节点创建类
class Node:
    def __init__(self, element=None):
        self.element = element
        self.next = None

    def get_element(self):
        return self.element
    
    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


## 链表类
class Linklist:

    # 初始化：只有头节点
    def __init__(self):
        self.head = Node()
        self.size = 0

    # 尾部插入
    def append(self, data):
        new_node = Node(data)  # 指向None
        # 遍历到尾部节点
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node


    # 头部插入
    def add(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head.next = new_node


    # 遍历链表并存储在数组
    def display(self):
        elems = []
        cur_node = self.head

        while cur_node.next != None:
            cur_node = cur_node.next 
            elems.append(cur_node.element)
            # cur_node = cur_node.next  
        print(elems)


    # 判断链表是否为空
    def is_empty(self):
        return self.size == 0
    
    
    # 遍历打印链表
    def travel(self):
        pass


    # 初始化链表
    def initList(self, data):
        pass


if __name__ == "__main__":
    l = Linklist()
    l.append(1)
    l.append(19) 
    l.display()
    


