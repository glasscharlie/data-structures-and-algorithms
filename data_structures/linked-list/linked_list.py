class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        return value
    def includes(self, value):
        if not self.head:
            return False
        cur = self.head
        while cur:
            if cur.value == value:
                return True
            cur = cur.next
        return False
    def to_string(self):
        value = " "
        cur = self.head
        while cur.next != None:
            value += " " + str(cur.value)
            cur = cur.next
        value += " " + str(cur.value)
        print(value)
        return value

    def insert_before(self, existing_value, value):
        
        current = self.head
        if current.value == existing_value:
            new_node = Node(value)
            new_node.next = current
            self.head = new_node
            return True

        while current.next:
            if current.next.value == existing_value:
                new_node = Node(value)
                new_node.next = current.next
                current.next = new_node
                return True
            current = current.next



    def insert_after(self, existing_value, value):
        current = self.head
        while current:
            if current.value == existing_value:
                new_node = Node(value)
                new_node.next = current.next
                current.next = new_node
                return True

            current = current.next    

    def append(self, value):
        if not self.head:
            self.insert(value)
            return
        else:
            current = self.head
        while current.next:
            current = current.next
        current.next = Node(value)

    
    def kth_from_end(self, k):
        value_list = []
        if self.head:
            current = self.head
            while current.next:
                value_list.append(current.value)
                current = current.next

            value_list.append(current.value)

        if 0 <= k < len(value_list):
            return value_list[-(k+1)]
        else:
            return 'K is out of range'

            
 
        q.head = q_curr
small_list = LinkedList()

small_list.insert(1)
small_list.insert(2)
small_list.insert(3)

# small_list.insert_after(2, 4)
# small_list.insert_before(2, 5)
# small_list.insert_before(9, 7)
# small_list.insert_after(9,7)
small_list.to_string()

big_list = LinkedList()

big_list.insert(4)
big_list.insert(5)
big_list.insert(6)
big_list.insert(6)
big_list.insert(7)
big_list.to_string()


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
    return a_list.head

        
        
        

# first list is longer
merge_list(big_list, small_list)
big_list.to_string()

#2nd list is longer
# merge_list(small_list, big_list)
# small_list.to_string()



