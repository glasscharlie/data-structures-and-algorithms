from stack_and_queues import Node, Stack, Queue

def test_Node():
  node = Node(1)
  expected = Node
  assert type(node) == expected

def test_push_one():
  stack = Stack()
  stack.push(1)
  expected = 1
  actual = stack.top.value
  assert expected == actual

def test_push_multiple():
  stack = Stack()
  stack.push('A')
  stack.push('B')
  stack.push('C')
  expected = True
  actual = stack.includes('B')
  assert expected == actual

def test_pop_one():
  stack = Stack()
  stack.push(1)
  stack.pop()
  expected = None
  actual = stack.top.value
  assert actual == expected

def test_pop_all():
  stack = Stack()
  stack.push(1)
  stack.push(2)
  stack.push(3)
  stack.pop()
  stack.pop()
  stack.pop()
  expected = None
  actual = stack.top.value
  assert actual == expected

def test_peek():
  stack = Stack()
  stack.push(1)
  stack.push(2)
  actual = stack.peek()
  expected = 2
  assert actual == expected

def test_Stack_empty():
  stack = Stack()
  actual = stack.top.value
  expected = None
  assert actual == expected

def test_enqueue_one():
  q = Queue()
  q.enqueue('Hello')
  expected = 'Hello'
  actual = q.front.value
  assert expected == actual

def test_enqueue_multiple():
  q = Queue()
  q.enqueue('A')
  q.enqueue('B')
  q.enqueue('C')
  expected = 'A'
  actual = q.front.value
  assert expected == actual

def test_dequeue_one():
  q = Queue()
  q.enqueue('A')
  q.enqueue('B')
  q.enqueue('C')
  q.rear.dequeue()
  q.front.dequeue()
  expected = 'B'
  actual = q.front.value
  assert expected == actual

def test_dequeue_all():
  q = Queue()
  q.enqueue('A')
  q.enqueue('B')
  q.enqueue('C')
  q.rear.dequeue()
  q.rear.dequeue()
  q.front.dequeue()
  expected = None
  actual = q.front.value
  assert expected == actual

def test_peek():
  q = Queue()
  q.peek(1)
  q.peek(2)
  actual = q.peek()
  expected = 2
  assert actual == expected


def test_Queue_empty():
  q = Queue()
  actual = q.front.value
  expected = None
  assert actual == expected
