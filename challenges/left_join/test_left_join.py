from left_join import left_join
from hashtable import Node, HashTable

def test_empy():
    first = HashTable()
    second = HashTable()
    actual = left_join(first, second)
    expected = []
    assert actual == expected

def test_no_repeats():
    first = HashTable()
    first.add('cat', 'meow')
    first.add('dog', 'woof')
    second = HashTable()
    second.add('snake', 'hiss')
    actual = left_join(first, second)
    expected = [('cat', 'meow', None), ('dog','woof', None)]
    assert actual == expected
def test_repeats():
    first = HashTable()
    first.add('cat', 'meow')
    first.add('dog', 'woof')
    second = HashTable()
    second.add('snake', 'hiss')
    second.add('cat', 'whiskers')
    actual = left_join(first, second)
    expected = [('cat', 'meow', 'whiskers'), ('dog','woof', None)]
    assert actual == expected