class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self, value):
        new_node = Node(value)
        if self.rear:
            self.rear.next = new_node
        else:
            self.front = new_node
        self.rear = new_node
    def dequeue(self):
        current = self.front
        if current != None:
            self.front = current.next
            return current
        else:
            print('Queue is empty.')
    def peek(self):
        if self.front == None:
            return None
        current = self.front
        return self.front.value
    def isEmpty(self):
        return self.front == None

class Node:
  def __init__(self, value=None):
    self.value = value
    self.left = None
    self.right = None
    self.next = None
    self.rear = None

class BinaryTree:
    def __init__(self, value=None):
        self._root = value

class BinarySearchTree():
    def __init__(self, value=None):
        self._root = value

    def add(self, value, current=None):

        if not self._root:
            self._root = Node(value)
            return

        if current is None:
            current = self._root

        if current:
            if value < current.value:
                if not current.left:
                    current.left = Node(value)
                else:
                    self.add(value, current.left)

            if value >= current.value:
                if not current.right:
                    current.right = Node(value)
                else:
                    self.add(value, current.right)


def breadth(tree): 

    if tree._root is None: 
        return None
      
    queue = Queue()
    lst = []

    queue.enqueue(tree._root) 
  
    while queue.front: 
        node = queue.front.value
        lst.append(node.value) 
  
        if node.left is not None: 
            queue.enqueue(node.left) 
  
        if node.right is not None: 
            queue.enqueue(node.right) 

        queue.dequeue()
        
    return lst


test = BinarySearchTree()
test.add(4)
test.add(3)
test.add(5)
test.add(9)
test.add(12)
test.add(2)
test.add(11)
print (breadth(test))

