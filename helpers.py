import itertools
from nltk.tokenize import sent_tokenize, word_tokenize


def lines(a, b):
    """Return lines in both a and b"""

    # TODO
    # Spilt each string inputs into lines
    # list_a = a.split('\n')
    # list_b = b.split('\n')
    # lst = []
    # for iter_a in list_a:
    #     for iter_b in list_b:
    #         if iter_a == iter_b:
    #             lst.append(iter_a)

    # remove duplicates
    # lst = list(dict.fromkeys(lst))
    # return lst
    # pythonic
    return set(a.split('\n')) & set(b.split('\n'))


def sentences(a, b):
    """Return sentences in both a and b"""

    # TODO
    # list_a = a.split('\n')
    # list_b = b.split('\n')
    # lst = []
    # for str_a in sent_tokenize(a):
    #     for str_b in sent_tokenize(b):
    #         if str_a == str_b:
    #             lst.append(str_a)
    # lst = list(dict.fromkeys(lst))
    # return lst
    #pythonic
    return list(set(sent_tokenize(a)).intersection(set(sent_tokenize(b))))




def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    # TODO
    seta = set()
    setb = set()
    x = []
    y = []
    for i in range(len(a) - n + 1):
        x.append(a[i:i+n])
        seta = set(x)

    for i in range(len(b) - n + 1):
        y.append(b[i:i+n])
        setb = set(y)
    # remove duplicates and retrun it
    return seta & setb

