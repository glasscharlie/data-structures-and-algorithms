class Node:
  def __init__(self, value=None):
    self.value = value
    self.left = None
    self.right = None

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


def make_copy(tree, current=None, new_copy=None):
    
    if new_copy == None:
        new_copy = BinarySearchTree()

    if not current:
        current = tree._root

    new_copy.add(current.value)
    
    if current.left:
        make_copy(tree, current.left, new_copy)

    if current.right:
        make_copy(tree, current.right, new_copy)


    return new_copy


def fizzbuzz_tree(tree, current=None, new=None):
    if tree._root == None:
        return BinarySearchTree()

    if new == None:
        new = make_copy(tree)
    if not current:
        current = new._root

    if current.value % 15 == 0:  
        current.value = "FizzBuzz"                                         
 
    elif current.value % 3 == 0:      
        current.value = "Fizz"                                         

    elif current.value % 5 == 0:          
        current.value = "Buzz" 
    
    else:  
        current.value = str(current.value)                                   

    if current.left:
        fizzbuzz_tree(new, current.left, new)

    if current.right:
       fizzbuzz_tree(new, current.right, new)

    return new

    def __init__(self, value=None):
        self._root = value



