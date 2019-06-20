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
        p = pListHead
        n = 0
        while p != None:
            n += 1
            p = p.next
        
        if k < 0 or k > n :
            return None
        else:
            q = pListHead
            for _ in range(n - k):
                q = q.next
            
            return q


        