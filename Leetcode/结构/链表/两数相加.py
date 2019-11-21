# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        cur = dummy # 这一步必须的，为了能从dummy返回整个链表，所以以cur替代dummy迭代
        C = 0

        while l1 or l2:
            if l1 and l2:
                S = l1.val + l2.val + C
                l1, l2 = l1.next, l2.next
            elif l1 is None:
                S = l2.val + 0 + C
                l2 = l2.next
            else:
                S = l1.val + 0 + C
                l1 = l1.next

            C = S // 10
            cur.next = ListNode(S % 10)
            cur = cur.next
        
        if C == 1:
            cur.next = ListNode(C)

        return dummy.next 


