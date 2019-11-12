'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
 
def sortList1(head):
    if not head or not head.next: return head
    # 找到中点
    slow, fast = head, head.next
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    mid, slow.next = slow.next, None
    # 划分
    l = sortList1(head)
    r = sortList1(mid)
    # 归并 哑变量
    h = res = ListNode(0)
    while l and r:
        if l.val < r.val:
            h.next, l = l, l.next
        else:
            h.next, r = r, r.next
        h = h.next # 这一步很关键
    h.next = l if l else r
    return res.next
'''

# O(1)空间复杂度
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        dummyhead = ListNode(0)
        dummyhead.next = head
        p, length = head, 0
        while p:
            length += 1
            p = p.next

        size = 1
        while size < length:
            cur = dummyhead.next
            tail = dummyhead
            while cur:
                left = cur
                right = self.split(left, size)
                cur = self.split(right, size)
                tail.next = self.merge(left, right)
                while tail.next:
                    tail = tail.next
            size += size
        return dummyhead.next
    # 函数
    def merge(self, left, right):
        p = res = ListNode(0)
        while left and right:
            if left.val < right.val:
                p.next = left
                left = left.next
            else:
                p.next = right
                right = right.next
            p = p.next
        p.next = left if left else right
        return res.next

    def split(self, head, n):
        while head and n-1:
            head = head.next
            n -= 1
        # 返回剩余节点
        if head is None: return None
        res = head.next
        head.next = None
        return res