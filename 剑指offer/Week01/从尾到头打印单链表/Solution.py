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