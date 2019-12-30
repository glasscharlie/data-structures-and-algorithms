def merge_list(a_list, b_list):
    a_list_curr = a_list.head 
    b_list_curr = b_list.head 
  
    while a_list_curr.next != None and b_list_curr != None: 
        #save the next address
        a_list_next = a_list_curr.next
        b_list_next = b_list_curr.next

        # make b_list_current next of a_list_curr 
        b_list_curr.next = a_list_next
        a_list_curr.next = b_list_curr 

        # update current for next iteration
        a_list_curr = a_list_next 
        b_list_curr = b_list_next
        
        #if a list doesnt have a next and b has a current
    if b_list_curr:
        a_list_curr.next = b_list_curr
