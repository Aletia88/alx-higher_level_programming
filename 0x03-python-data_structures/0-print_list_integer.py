#!/usr/bin/bash

def print_list_integer(my_list=[]):
    length = len(my_list)
    i = 0
    while (length > i):
        print("{}" .format(my_list[i]))
        i = i + 1
