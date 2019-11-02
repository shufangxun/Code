def reverse1(head):
    # 从前往后反转各个结点的指针域的指向
    pre = None
    cur = head

    while cur:
        nex = cur.next   # 先将cur的下一个节点存储
        cur.next = pre   # 将cur的指针指向上一个节点
        pre = cur        # 移动指针：当前指针变成前一个
        cur = nex        # 下一个指针变成当前
    return pre
    
def reverse2(head):
    
    if not head or not head.next:
        return head
        
    p = reverse2(head.next)
    next_node = head.next    #        head -> next_node 
    next_node.next = head    #        head <- next_node 
    head.next = None         # [x] <- head <- next_node 
    return p