from array_binary_search import binary_search

#tests if search numbers equal to numbers in the array return the index that number is found at
def test_index_one():
    expected = 0
    actual = binary_search([0,5,10,15,20, 25], 0)
    assert actual == expected
    
def test_index_two():
    expected = 1
    actual = binary_search([0,5,10,15,20, 25], 5)
    assert actual == expected

def test_index_three():
    expected = 2
    actual = binary_search([0,5,10,15,20, 25], 10)
    assert actual == expected

def test_index_Four():
    expected = 3
    actual = binary_search([0,5,10,15,20, 25], 15)
    assert actual == expected

# tests for search values not in array to return -1
def test_not_in_index_one():
    expected = -1
    actual = binary_search([0,5,10,15,20, 25], 3)
    assert actual == expected

def test_not_in_index_two():
    expected = -1
    actual = binary_search([0,5,10,15,20, 25], 57)
    assert actual == expected

def test_not_in_index_three():
    expected = -1
    actual = binary_search([0,5,10,15,20, 25], 257)
    assert actual == expected