# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def findKthToTail(self, pListHead, k):
        """
        :type pListHead: ListNode
        :type k: int
        :rtype: ListNode
        """
        fast = slow = pListHead

        for _ in range(k):
            if fast is None:
                return None
            fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next 
        return slow