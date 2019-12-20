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
  tree.add(10)
  tree.add(15)
  expected = [5, 10, 15]
  actual = tree.pre_order()
  assert actual == expected

def test_pre_order_more():
    tree = BinarySearchTree()
    tree.add(5)
    tree.add(10)
    tree.add(15)
    tree.add(20)
    # tree.add(25)
    # tree.add(30)
    # tree.add(35)
    # tree.add(40)
    # tree.add(45)
    # tree.add(50)
    # tree.add(55)
    # tree.add(60)
    # tree.add(65)
    # tree.add(70)
    # tree.add(75)
    # tree.add(80)
    # tree.add(85)

    assert tree._root.value == 5
    assert not tree._root.left
    assert tree._root.right.value == 10
    assert not tree._root.right.left
    assert tree._root.right.right.value == 15
    assert not tree._root.right.right.left
    assert tree._root.right.right.right.value == 20
    assert not tree._root.right.right.right.left
    # expected = [5, 10, 15, 20] #25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85 ]
    # actual = tree.pre_order()
    # assert actual == expected

def test_in_order_three():
    tree = BinarySearchTree()
    tree.add(5)
    tree.add(10)
    tree.add(15)
    expected = [5, 10, 15]
    actual = tree.in_order()
    assert actual == expected

# def test_in_order_more():
#     tree = BinarySearchTree()
#     tree.add(5)
#     tree.add(10)
#     tree.add(15)
#     tree.add(20)
#     tree.add(25)
#     tree.add(30)
#     tree.add(35)
#     tree.add(40)
#     tree.add(45)
#     tree.add(50)
#     tree.add(55)
#     tree.add(60)
#     tree.add(65)
#     tree.add(70)
#     tree.add(75)
#     tree.add(80)
#     tree.add(85)
#     expected = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85 ]
#     actual = tree.in_order()
#     assert actual == expected