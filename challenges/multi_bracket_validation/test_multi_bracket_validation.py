from multi_bracket_validation import validation

def test_null():
    assert validation('') == True

def test_open_close():
    assert validation('()') == True

def test_open_close_two():
    assert validation('{]') == False
    assert validation('{)') == False
    assert validation('[)') == False
    assert validation('[}') == False

def test_open_close_three():
    assert validation('({[]})') == True

def test_no_close():
    assert validation('({[]})(') == False

def test_open():
    assert validation('({[') == False

def test_no_close_two():
    assert validation('(({[[()]]})') == False

def test_words():
    assert validation('(abc[123{lmnop[hello_world(3)[4]]}])') == True

def test_middle():
    assert validation('({[(])})') == False