from quick_sort import quick_sort

def test_unique_values():
    lst = [8,4,23,42,16,15]
    expected = [4,8,15,16,23,42]
    actual = quick_sort(lst)
    assert actual == expected

def test_duplicate_value():
    lst = [8,4,23,42,16,15,8,23]
    expected = [4,8,8,15,16,23,23,42]
    actual = quick_sort(lst)
    assert actual == expected

def test_negative_values():
    lst = [8,4,23,-42,16,-15]
    expected = [-42,-15,4,8,16,23]
    actual = quick_sort(lst)
    assert actual == expected