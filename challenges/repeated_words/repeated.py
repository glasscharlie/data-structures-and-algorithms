from collections import Counter

def punctuation(str):
    punc = '.,;!/?#:@$%&'
    new_str = ""
    for i in str:
        if i not in punc:
            new_str += i
    return new_str

def repeated_word(str):
    string = punctuation(str)
    string = string.casefold()
    new_str = string.split(' ')
    dict = Counter(new_str)
    for i in new_str:
        if dict[i] > 1:
            return i
    return false


