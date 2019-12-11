import pytest
from linked_list import linked_list, Node


my_list = linked_list()

def test_make_node():
    expected = Node
    actual = Node(3)
    assert type(actual) == expected

def test_includes_true():
    expected = True
    my_list.insert(12)
    actual = my_list.includes(12)
    assert actual == expected

def test_includes_false():
    my_list = linked_list()
    expected = False
    my_list.insert(12)
    actual = my_list.includes(13)
    assert actual == expected

def test_to_string_one():
    expected = '  3 2 1'
    my_list = linked_list()
    my_list.insert(1)
    my_list.insert(2)
    my_list.insert(3)
    actual = my_list.to_string()
    assert actual == expected

def test_to_string_two():
    expected = '  1'
    my_list = linked_list()
    my_list.insert(1)
    actual = my_list.to_string()
    assert actual == expected

def test_insert_one():
    expected = 3
    my_list.insert(3)
    my_list.to_string()
    actual = my_list.head.data
    assert actual == expected

def test_insert_two():
    expected = 5
    my_list.insert(3)
    my_list.insert(4)
    my_list.insert(5)
    my_list.to_string()
    actual = my_list.head.data
    assert actual == expected


def test_append_one():
    my_list = linked_list()
    expected = 1
    my_list.append(1)
    assert my_list.includes(1) == True


def test_append_two():
    my_list = linked_list()
    my_list.insert(1)
    my_list.insert(2)
    my_list.append(3)
    assert my_list.includes(3) == True

def test_insert_before():
    my_list = linked_list()
    my_list.insert(1)
    my_list.insert(2)
    my_list.insert_before(1, 3)
    assert my_list.to_string() == True



# Where k is greater than the length of the linked list
def test_k_is_greater_than_length():
    my_list = linked_list()
    my_list.insert(2)
    my_list.insert(8)
    my_list.insert(3)
    my_list.insert(1)
    assert my_list.kth_from_end(20) == 'K is out of range'
# Where k and the length of the list are the same
def test_k_is_same_length():
    my_list = linked_list()
    assert my_list.kth_from_end(6) == 'K is out of range'
# Where k is not a positive integer
def test_k_is_negative():
    my_list = linked_list()
    assert my_list.kth_from_end(-4) == 'K is out of range'
# Where the linked list is of a size 1
def test_k_is_in_list_of_one():
    my_list = linked_list()
    my_list.insert(2)
    assert my_list.kth_from_end(0) == 2
# "Happy Path" where k is not at the end, but somewhere in the middle of the linked list
def test_k_is_happy():
    my_list = linked_list()
    my_list.insert(2)
    my_list.insert(8)
    my_list.insert(3)
    my_list.insert(1)
    assert my_list.kth_from_end(2) == 3



@pytest.fixture(autouse=True)
def clean():
    my_list = []