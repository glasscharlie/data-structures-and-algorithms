class _Node:
  def __init__(self, value=None):
    self.value = value
    self.left = None
    self.right = None
    self.next = None
    self.rear = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self, value):
        new_node = _Node(value)
        if self.rear:
            self.rear.next = new_node
        else:
            self.front = new_node
        self.rear = new_node
    def dequeue(self):
        current = self.front
        if current != None:
            self.front = current.next
            return current.value
        else:
            print('Queue is empty.')
    def peek(self):
        if self.front == None:
            return None
        current = self.front
        return self.front.value
    def is_empty(self):
        return self.front == None


class BinaryTree:
    def __init__(self, value=None):
        self._root = value

    def pre_order(self, current=None, output_array=None):
        if output_array == None:
            output_array = []
        
        if not current:
            current = self._root

        output_array.append(current.value)

        if current.left:
            self.pre_order(current.left, output_array)

        if current.right:
            self.pre_order(current.right, output_array)

        return output_array

    def in_order(self, current=None, output_array=None):
        if output_array == None:
            output_array=[]
        if not current:
            current = self._root

        if current.left:
            self.in_order(current.left, output_array)

        output_array.append(current.value)

        if current.right:
            self.in_order(current.right, output_array)

        return output_array

    def post_order(self, current=None, output_array=None):
        if output_array == None:
            output_array=[]

        if not current:
            current = self._root

        if current.left:
            self.post_order(current.left, output_array)

        if current.right:
            self.post_order(current.right, output_array)

        output_array.append(current.value)

        return output_array

    def add(self, value):

        node = _Node(value)

        if not self._root:
            self._root = node
            return

        q = Queue()

        q.enqueue(self._root)
        while not q.is_empty():

            current = q.dequeue()
            print('current: ', current.value)

            if current.left:
                q.enqueue(current.left)
            else:
                current.left = node
                print('left: ', current.left.value)
                break

            if current.right:
                q.enqueue(current.right)
            else:
                current.right = node
                print('right: ', current.right.value)
                break



    def find_maximum_value(self, highest=None, current=None):

        if not self._root:
            return None
            
        if not current:
            current = self._root

        if highest == None:
            highest = self._root.value

        if current.left:
            highest = self.find_maximum_value(highest, current.left)

        if current.right:
            highest = self.find_maximum_value(highest, current.right)

        if current.value > highest:
            highest = current.value

        print(highest, current.value)    

        return highest

  

