from array_shift import add_to_middle

def test_one():
    expected = [0,1,2,8,3,4]
    actual = add_to_middle([0,1,2,3,4], 8)
    assert actual == expected

def test_two():
    expected = [0,1,2,8,3,4,5]
    actual = add_to_middle([0,1,2,3,4, 5], 8)
    assert actual == expected