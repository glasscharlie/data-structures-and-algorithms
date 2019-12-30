from breadth import Node, BinarySearchTree, BinaryTree, breadth

def test_empty_tree():
    tree = BinarySearchTree()
    actual = breadth(tree)
    expected = None
    assert actual == expected

def test_one():
    tree = BinarySearchTree()
    tree.add(11)
    actual = breadth(tree)
    expected = [11]
    assert actual == expected

def test_three():
    tree = BinarySearchTree()
    tree.add(11)
    tree.add(9)
    tree.add(15)
    actual = breadth(tree)
    expected = [11, 9, 15]
    assert actual == expected

def test_more():
    tree = BinarySearchTree()
    tree.add(11)
    tree.add(9)
    tree.add(5)
    tree.add(10)
    tree.add(15)
    tree.add(13)
    tree.add(17)
    actual = breadth(tree)
    expected = [11, 9, 15, 5, 10, 13, 17]
    assert actual == expected

