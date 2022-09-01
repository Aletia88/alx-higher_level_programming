#!/usr/bin/python3
def search_replace(my_list, search, replace):
    _newlist = my_list.copy()
    for i in range(len(_newlist)):
        if _newlist[i] == search:
            _newlist[i] = replace
    return _neewlist
