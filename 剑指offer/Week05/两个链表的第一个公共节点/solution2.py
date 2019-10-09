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
        stackA = []
        stackB = []

        while headA:
            stackA.append(headA)
            headA = headA.next
        while headB:
            stackB.append(headB)
            headB = headB.next

        pre = None
        while stackA and stackB and stackA[-1] == stackB[-1]:
            pre = stackA.pop()
            stackB.pop()

        return pre
        