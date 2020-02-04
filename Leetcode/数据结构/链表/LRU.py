# 结点：包括key和value
# key 用来和哈希表连接
class ListNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.pre = None
        self.nex = None

# 双向链表
class Dlinklist:
    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.nex = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def addFirst(self, node):
        # 先把前后结点安排好
        node.nex = self.head.nex
        node.pre = self.head
        # 再操作前后结点的指向
        self.head.nex.pre = node
        self.head.nex = node
        self.size += 1
    
    def remove(self, node):
        node.pre.nex = node.nex
        node.nex.pre = node.pre
        self.size -= 1

    def removeLast(self):
        if self.tail.pre == self.head:
            return None
        last = self.tail.pre
        self.remove(last)
        return last
    

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {} # 形式 {key: node(key,value,pre,nex),...}
        self.cache = Dlinklist()

    def get(self, key: int) -> int:
        if key not in self.map.keys():
            return -1
        val = self.map.get(key).value
        self.put(key, val)
        return val
        
    def put(self, key: int, value: int) -> None:
        node = ListNode(key, value)
        if key in self.map.keys():
            # 删除存在结点而不是新建结点node
            # 得到node:map.get(key)
            self.cache.remove(self.map.get(key))
            self.cache.addFirst(node)
            self.map.update({key:node})
        else:
            if self.capacity == self.cache.size:
                last = self.cache.removeLast()
                self.map.pop(last.key)
            self.cache.addFirst(node)
            self.map.update({key:node})

        
