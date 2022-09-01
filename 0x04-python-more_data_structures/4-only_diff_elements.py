#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    a = set()
    for i in set_1:
        if i in set_2:
            continue
        else:
            a.add(i)
    for i in set_2:
        if i in set_1:
            continue
        else:
            a.add(i)
    return
