from find_maximum_value import _Node, BinaryTree

# def test_empty():
#     tree = BinaryTree()
#     actual = tree.find_maximum_value()
#     expected = None
#     assert actual == expected

# def test_one():
#     tree = BinaryTree()
#     tree.add(11)
#     actual = tree.find_maximum_value()
#     expected = 11
#     assert actual == expected

# def test_three():
#     tree = BinaryTree()
#     tree.add(5)
#     tree.add(15)
#     tree.add(3)
#     actual = tree.pre_order()
#     expected = 15
#     assert actual == expected

# def test_more():
#     tree = BinaryTree()
#     tree.add(22)
#     tree.add(5)
#     tree.add(3)
#     tree.add(11)
#     tree.add(2)
#     tree.add(13)
#     actual = tree.in_order()
#     expected = 5
#     assert actual == expected


# def test_multiples():
#     tree = BinarySearchTree()
#     tree.add(5)
#     tree.add(3)
#     tree.add(11)
#     tree.add(2)
#     tree.add(11)
#     tree.add(11)
#     tree.add(11)
#     tree.add(11)
#     tree.add(11)
#     tree.add(11)
#     tree.add(11)
#     tree.add(11) 
#     actual = tree.find_maximum_value()
#     expected = 11
#     assert actual == expected

def test_add_four():
    tree = BinaryTree()
    tree.add('apples')
    tree.add('oranges')
    print(tree._root.left)
    # tree.add('peaches')
    # tree.add('bananas')
    assert tree._root.value == 'apples'
    assert tree._root.left.value == 'oranges'
    
    # assert tree._root.right.value == 'peaches'
    # assert tree._root.left.left.value == 'bananas'