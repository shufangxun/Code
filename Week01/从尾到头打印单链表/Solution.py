# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def printListReversingly(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        p = head
        res = []
        while p :
            res.insert(0,p.val)
            p = p.next
        return res