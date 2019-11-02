class DListNode:
    def __init__(self, val):
        self.val = val
        self.pre = None
        self.next = None

    def reverse(self, head):
        pre = None
        cur = head
        while cur:
            nex = cur.next
            cur.next = cur.pre
            cur.pre = nex

            pre = cur
            cur = nex
        return pre