# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 对于逆序的问题，考虑栈
        s1, s2 = [], []

        # 压栈
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next

        ans = None
        c = 0

        while s1 or s2 or c != 0:
            a = 0 if not s1 else s1.pop()
            b = 0 if not s2 else s2.pop()
            cursum  = a + b + c
            c = cursum // 10
            cursum %= 10
            
            curnode = ListNode(cursum)
            curnode.next = ans
            ans = curnode
        return ans
