#!/usr/bin/python3
"""MyList class"""


class MyList(list):
    """ defining a function that return a sorted list"""
    def print_sorted(self):
        print(sorted(self))
