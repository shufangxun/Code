# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def _length(self, head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count
    def findFirstCommonNode(self, headA, headB):
        """
        :type headA, headB: ListNode
        :rtype: ListNode
        """
        countA, countB = self._length(headA), self._length(headB)
        k = abs(countA - countB)

        if countA > countB:
            for i in range(k):
                headA = headA.next
        else:
            for i in range(k):
                headB = headB.next
        
        while headA != headB and headA and headB: ## 一个好的技巧，不需要break和多个条件语句
            headA = headA.next
            headB = headB.next
        
        return headA 
            

        

        
        




            
