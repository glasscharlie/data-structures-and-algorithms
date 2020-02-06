from tree import Node, BinarySearchTree


def intersection(tree, tree_2):
    lst = []
    new_set = set()
    def traverse(node, second_tree):
        if not node:
            return
        traverse(node.left, second_tree)
        traverse(node.right, second_tree)
        if second_tree:
            if node.value in new_set:
                lst.append(node.value)
        else:
            new_set.add(node.value)

    traverse(tree._root, False)
    traverse(tree_2._root, True)
    return lst