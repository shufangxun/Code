def reverse2(head):
    
    if not head or not head.next:
        return head
        
    new_head = reverse2(head.next)
    next_node = head.next    #        head -> next_node 
    next_node.next = head    #        head <- next_node 
    head.next = None         # [x] <- head <- next_node 
    return new_head