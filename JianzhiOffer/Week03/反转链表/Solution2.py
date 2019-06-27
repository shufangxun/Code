# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 递归法 每一次反转当前节点
        # 将当前节点的下一个节点的指针域指向自己，并将自身的指针域指向空
        # 注意返回的是整个头结点
        if head is None or head.next is None:
            return head
        
        p = self.reverseList(head.next)
        old_nex = head.next
        old_nex.next = head
        head.next = None

        return p
