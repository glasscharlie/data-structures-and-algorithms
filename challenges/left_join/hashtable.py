init_size = 50

class Node:
    """node Class"""
    def __init__(self, key, value):
        """initialized the node class with a key, value and next properties"""
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    """hashtable class"""
    def __init__(self):
        """initializes the hashtable with a capacity, size and bucket"""
        self.capacity = init_size
        self.size = 0
        self.bucket = [None]*self.capacity
    def hash(self, key):
        """hash method to return an index in the collection for a given key"""
        hashsum = 0
        for idx, c in enumerate(key):
            hashsum += (idx + len(key)) ** ord(c)
            hashsum = hashsum % self.capacity
        return hashsum


    def add(self, key, value):
        """takes in both the key and value. This method should hash the key, and add the key and value pair to the table, handling collisions as needed."""
        self.size += 1
        index = self.hash(key)
        node = self.bucket[index]
        if node is None:
            self.bucket[index] = Node(key, value)
            return
        prev = node 
        while node is not None:
            prev = node 
            node = node.next
        prev.next = Node(key, value)

    def get(self, key):
        """takes in the key and returns the value from the table """
        index = self.hash(key)
        node = self.bucket[index]
        while node != None and node.key != key:
            node = node.next
        if node is None:
            return None
        else:
            return node.value

    def contains(self, key):
        """takes in the key and returns a boolean, indicating if the key exists in the table already."""
        index = self.hash(key)
        node = self.bucket[index]
        if node == None:
            return False
        else:
            return True