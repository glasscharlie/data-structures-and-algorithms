from trees import BinarySearchTree, BinaryTree

def test_tree_instance():
  tree = BinaryTree()
  assert tree._root == None

def test_tree_one_member():
  tree = BinarySearchTree()
  tree.add('apples')
  assert tree._root.value == 'apples'

def test_three_members():
  tree = BinarySearchTree()
  tree.add(10)
  tree.add(5)
  tree.add(15)
  assert tree._root.value == 10
  assert tree._root.left.value == 5
  assert tree._root.right.value == 15

def test_pre_order_three():
    tree = BinarySearchTree()
    tree.add(5)
    tree.add(3)
    tree.add(15)
    expected = [5, 3, 15]
    actual = tree.pre_order()
    assert actual == expected

def test_pre_order_more():
    tree = BinarySearchTree()
    tree.add(20)
    tree.add(5)
    tree.add(10)
    tree.add(15)
    tree.add(25)
    tree.add(35)
    tree.add(40)
    tree.add(23)
    tree.add(45)


    # assert tree._root.value == 5
    # assert not tree._root.left
    # assert tree._root.right.value == 10
    # assert not tree._root.right.left
    # assert tree._root.right.right.value == 15
    # assert not tree._root.right.right.left
    # assert tree._root.right.right.right.value == 20
    # assert not tree._root.right.right.right.left

    expected = [20, 5, 10, 15, 25, 23, 35, 40, 45]
    actual = tree.pre_order()
    assert actual == expected

def test_in_order_three():
    tree = BinarySearchTree()
    tree.add(5)
    tree.add(3)
    tree.add(15)
    expected = [3, 5, 15]
    actual = tree.in_order()
    assert actual == expected

def test_in_order_more():
    tree = BinarySearchTree()
    tree.add(20)
    tree.add(5)
    tree.add(10)
    tree.add(15)
    tree.add(25)
    tree.add(35)
    tree.add(40)
    tree.add(23)
    tree.add(45)
    expected = [5, 10, 15, 20, 23, 25, 35, 40, 45]
    actual = tree.in_order()
    assert actual == expected

def test_post_order_three():
    tree = BinarySearchTree()
    tree.add(5)
    tree.add(3)
    tree.add(15)
    expected = [3, 15, 5]
    actual = tree.post_order()
    assert actual == expected

def test_in_order_more():
    tree = BinarySearchTree()
    tree.add(20)
    tree.add(5)
    tree.add(10)
    tree.add(15)
    tree.add(25)
    tree.add(35)
    tree.add(40)
    tree.add(23)
    tree.add(45)
    expected = [15, 10, 5, 23, 45, 40, 35, 25, 20]
    actual = tree.post_order()
    assert actual == expected

def test_contains_one():
    tree = BinarySearchTree()
    tree.add(20)
    expected = True
    actual = tree.contains(20)
    assert actual == expected

def test_contains_three_left():
    tree = BinarySearchTree()
    tree.add(20)
    tree.add(30)
    tree.add(10)
    expected = True
    actual = tree.contains(10)
    assert actual == expected

def test_contains_three_right():
    tree = BinarySearchTree()
    tree.add(20)
    tree.add(30)
    tree.add(10)
    expected = True
    actual = tree.contains(30)
    assert actual == expected

def test_contains_lots():
    tree = BinarySearchTree()
    tree.add(20)
    tree.add(15)
    tree.add(24)
    tree.add(16)
    tree.add(14)
    tree.add(22)
    tree.add(30)
    expected = True
    actual = tree.contains(16)
    assert actual == expected