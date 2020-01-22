class Node:
  def __init__(self, value=None):
    self.value = value
    self.left = None
    self.right = None

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
    

def tree_insertion(tree, other_tree):

    if tree.root == None or other_tree.root == None:
        return False

    lst = tree.pre_order()
    other_list = other_tree.pre_order()

    output = []

    for i in lst:
        if i in other_list:
            output.append(i)
    return output
