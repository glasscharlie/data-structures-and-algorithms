class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
class Stack(top):
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
        else:
            print(“Stack is empty.“)
    def peek(self):
        current = self.top
        return current.data
    def isEmpty(self):
        return self.top == None
class Queue:
    def __init__(self:
        self.front = None
        self.rear = None
    def enqueue(self, item):
        new_node = Node(item)
        if self.rear:
            self.rear.next = new_node
        else:
            self.front = new_node
        self.rear = new_node
        self.count = self.count + 1
    def dequeue(self):
        current = self.front
        if current != None:
            self.front = current.next
            self.count = self.count - 1
        else:
            print(“Queue is empty.“)
    def peek(self):
        current = self.front
        return self.front.data
    def isEmpty(self):
        return self.front == None