# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def findFirstCommonNode(self, headA, headB):
        """
        :type headA, headB: ListNode
        :rtype: ListNode
        """
        pa = headA
        pb = headB

        while pa != pb:
            pa = pa.next if pa else headB
            pb = pb.next if pb else headA
        
        return pa