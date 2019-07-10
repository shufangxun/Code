# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplication(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 保留一个重复结点
        if head is None or head.next is None:
            return head
        
        H = ListNode(-1)

        pre = H
        pre.next = head
        cur = head

        while cur and cur.next:
            if cur.val == cur.next.val:
                pre = cur
                curRep = cur.val
                while cur and cur.val == curRep:
                    cur = cur.next
                
                pre.next = cur
            else:
                pre = cur
                cur = cur.next
        
        return H.next



    

        