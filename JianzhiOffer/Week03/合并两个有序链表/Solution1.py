# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def merge(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 递归法 注意判断条件是两个if
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        p = None
        if l1.val < l2.val:
            p = l1
            p.next = self.merge(l1.next, l2)
        else:
            p = l2
            p.next = self.merge(l1, l2.next)

        return p