from linked_list import LinkedList, Node
from ll_merge import merge_list

def test_merge_same_size():
    my_list = LinkedList()
    my_list.insert(3)
    my_list.insert(2)
    my_list.insert(1)
    other_list = LinkedList()
    other_list.insert(6)
    other_list.insert(5)
    other_list.insert(4)
    merge_list(my_list, other_list)
    assert my_list.to_string() == '  1 4 2 5 3 6'

def test_first_is_bigger():
    my_list = LinkedList()
    my_list.insert(4)
    my_list.insert(3)
    my_list.insert(2)
    my_list.insert(1)
    other_list = LinkedList()
    other_list.insert(6)
    other_list.insert(5)
    merge_list(my_list, other_list)
    assert my_list.to_string() == '  1 5 2 6 3 4'

def test_second_is_bigger():
    my_list = LinkedList()
    my_list.insert(2)
    my_list.insert(1)
    other_list = LinkedList()
    my_list.insert(4)
    my_list.insert(3)
    other_list.insert(6)
    other_list.insert(5)
    merge_list(my_list, other_list)
    assert my_list.to_string() == '  3 5 4 6 1 2'