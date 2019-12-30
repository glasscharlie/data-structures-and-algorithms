class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
class Stack():
    def __init__(self):
        self.top = None
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
    def pop(self):
        current = self.top
        if current:
            self.top = current.next
            return current.value
        else:
            print('Stack is empty.')
    def peek(self):
        if self.top == None:
            return None
        else: 
            current = self.top
            return current
    def isEmpty(self):
        return self.top == None

class Queue:
    def __init__(self):
        self.inbox = Stack()
        self.outbox = Stack()
 
    def enqueue(self, data):
        self.inbox.push(data)
 
    def dequeue(self):
        while self.inbox.peek() != None:
            popped = self.inbox.pop().value
            self.outbox.push(popped)
        return self.outbox.pop()

# test = Queue()

# test.enqueue(1)
# test.enqueue(2)
# test.enqueue(3)
# test.enqueue(4)

def testprint():
    test = Queue()

    test.enqueue(10)
    test.enqueue(20)
    test.enqueue(30)
    test.dequeue
    print()


testprint()
