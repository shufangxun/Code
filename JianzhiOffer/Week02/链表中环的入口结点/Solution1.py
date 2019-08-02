# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def entryNodeOfLoop(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head.next
        while p:
            if p.next == p:
                return p.val
            p = p.next

        return None
        

