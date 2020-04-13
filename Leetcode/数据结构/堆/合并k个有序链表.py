class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        import heapq
        que = []  # que 存K个链表滑动的头指针
        for index, l in enumerate(lists):
                if l != None:
                    # python的问题，不能存结点，存索引吧
                    heapq.heappush(que ,(l.val, index))

        dummy_node = ListNode(-1)
        merged = dummy_node
        while que:
            val, index = heapq.heappop(que)
            merged.next = ListNode(val)
            merged = merged.next
            # 对应存索引
            lists[index] = lists[index].next
            if lists[index] != None:
                heapq.heappush(que, (lists[index].val, index))
        return dummy_node.next