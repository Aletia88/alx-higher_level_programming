#!/usr/bin/python3
def multiple_returns(sentence):
    my_tuple = ()
    a = list(sentence)
    if len(a) == 0:
        a[0] = None
    my_tuple = len(a), a[0]
    return my_tuple
