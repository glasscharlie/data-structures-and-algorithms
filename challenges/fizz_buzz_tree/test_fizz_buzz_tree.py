from fizz_buzz_tree import Node, BinarySearchTree, BinaryTree, make_copy, fizzbuzz_tree



def test_Values():
    tree = BinarySearchTree()
    tree.add(15)
    tree.add(10)
    tree.add(27)
    tree.add(17)
    tree.add(1)
    assert fizzbuzz_tree(tree)._root.value == 'FizzBuzz'
    assert fizzbuzz_tree(tree)._root.left.value == 'Buzz'
    assert fizzbuzz_tree(tree)._root.right.value == 'Fizz'
    assert fizzbuzz_tree(tree)._root.left.left.value == '1'
    assert fizzbuzz_tree(tree)._root.right.left.value == '17'

def test_empty_list():
    tree = BinarySearchTree()
    assert fizzbuzz_tree(tree)._root == None