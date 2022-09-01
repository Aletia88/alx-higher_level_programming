#!/usr/bin/python3
def uniq_add(my_list=[]):
    _sum = 0
    set_list = set(my_list)
    for i in set_list:
        _sum += i
    return _sum
