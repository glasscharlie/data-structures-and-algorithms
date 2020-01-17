from hashtable import HashTable, Node

# Adding a key/value to your hashtable results in the value being in the data structure
def test_value_added():
    hash = HashTable()
    hash.add('cat', 'meow')
    expected = 1
    actual = hash.size
    assert actual == expected
# Retrieving based on a key returns the value stored
def test_value_retrieved():
    hash = HashTable()
    hash.add('cat', 'meow')
    expected = 'meow'
    actual = hash.get('cat')
    assert actual == expected
# Successfully returns null for a key that does not exist in the hashtable
def test_value_not_included():
    hash = HashTable()
    hash.add('cat', 'meow')
    expected = False
    actual = hash.contains('dog')
    assert actual == expected
# Successfully handle a collision within the hashtable
def test_collision_handled():
    hash = HashTable()
    hash.add('cat', 'meow')
    hash.add('atc', 'value')
    actual = 2
    expected = hash.size
    assert actual == expected
# Successfully retrieve a value from a bucket within the hashtable that has a collision
def test_collision_retrieved():
    hash = HashTable()
    hash.add('cat', 'meow')
    hash.add('atc', 'value')
    actual = 'value'
    expected = hash.get('atc')
    assert actual == expected
# Successfully hash a key to an in-range value
def test_hash_key():
    hash = HashTable()
    expected = hash.hash('test hash')
    actual = 27
    assert actual == expected
