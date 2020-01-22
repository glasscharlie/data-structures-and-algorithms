from tree_insertion import Node, BinarySearchTree, tree_insertion

def test_node():
    node = Node(3)
    actual = node.value
    expected = 3
    assert actual == expected