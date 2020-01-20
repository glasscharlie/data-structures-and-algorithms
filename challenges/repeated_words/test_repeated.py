from repeated import repeated_word, punctuation

def test_punctuation_function():
    string = 'My, dog! ate. my? #homework'
    actual = punctuation(string)
    expected = 'My dog ate my homework'
    assert actual == expected

def test_lowercase_string():
    string = 'My dog ate my homework!'
    actual = repeated_word(string)
    expected = 'my'
    assert actual == expected

def test_capitols():
    string = 'My Dog ATE mY homework!'
    actual = repeated_word(string)
    expected = 'my'
    assert actual == expected

def test_punctuation_repeated():
    string = 'My, dog! ate. my? #homework'
    actual = repeated_word(string)
    expected = 'my'
    assert actual == expected

def test_multiple_repeated():
    string = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    actual = repeated_word(string)
    expected = 'it'
    assert actual == expected