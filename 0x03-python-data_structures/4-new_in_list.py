#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if (idx < 0 // idx > len(my_list) -1):
        return my_list
    else:
        orginal = my_list.copy()
        orginal[idx] = element
        return orginal
