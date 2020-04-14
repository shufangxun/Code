# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return 
        n = len(lists)
        return self.merge(lists, 0, n - 1)
    
    # 分链表 递归做法
    def merge(self, lists, left, right):
        if left == right:
            return lists[left]
        mid = left + (right - left) // 2
        l1 = self.merge(lists, left, mid)
        l2 = self.merge(lists, mid+1, right)
        return self.mergeTwoLists(l1, l2)

    # 合并两个链表
    def mergeTwoLists(self, l1, l2):
        dummyhead = ListNode(0)
        p = dummyhead
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        p.next = l1 if l1 else l2
        return dummyhead.next

# 循环做法 
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        n = len(lists)
        sz = 1
        while sz < n:
            for i in range(0, n - sz, sz * 2):
                lists[i] = self.merge(lists[i], lists[i + sz])
            sz *= 2

        return lists[0] if n > 0 else lists 

    def merge(self, l, r):
        dummyNode = ListNode(-1)
        head = dummyNode
        while l and r:
            if l.val < r.val:
                head.next = l
                l = l.next
            else:
                head.next = r
                r = r.next
            # 关键
            head = head.next
        head.next = l if l else r
        return dummyNode.next
