class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class linked_list:
    def __init__(self):
        self.head = None
    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        return data
    def includes(self, data):
        if not self.head:
            return False
        cur = self.head
        while cur:
            if cur.data == data:
                return True
            cur = cur.next
        return False
    def to_string(self):
        value = " "
        cur = self.head
        while cur.next != None:
            value += " " + str(cur.data)
            cur = cur.next
        value += " " + str(cur.data)
        print(value)
        return value

    def insert_before(self, data, new_val):
        if self.includes(data):
            new_node = Node(data)
            current = self.head
            while current.next:
                if current.next.data == data:
                    new_node = current.next
                    current.next = new_node.next
                    return self.__str__()
                else:
                    current = current.next
                    return self.__str__()


    def insert_after(self, existing, val):
        if self.includes(existing):
            current = self.head
            while current:
                if current.val == existing:
                    new_node = current.next
                    new_node.next = current.next
                    return self.__str__()
                else:
                    current = current.next
                    return self.__str__()

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
                value_list.append(current.data)
                current = current.next

            value_list.append(current.data)

        if 0 <= k < len(value_list):
            return value_list[-(k+1)]
        else:
            return 'K is out of range'
