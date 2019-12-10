class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class linked_list:
    def __init__(self):
        self.head = Node()
    def insert_before(self, data):
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
        print(value)
        return value

    def insert_after(self, desired_location):
        new_node = Node(desired_location)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def append(self, val):
        current = self.head
        while current:
            if current.next == None:
                current.next = Node(val)
                return self.__str__()
            else:
                current = current.next
                self.head = Node(val)
                return self.__str__()
