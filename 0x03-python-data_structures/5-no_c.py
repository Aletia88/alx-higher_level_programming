#!/usr/bin/python3
def no_c(my_string):
    x = ""
    y = ""
    z = "cC"
    mytable = my_string.maketrans(x, y, z)
    new_str = my_string.translate(mytable)
    return new_str
