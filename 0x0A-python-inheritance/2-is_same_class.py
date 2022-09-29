#!/usr/bin/python3
""" defining a function is_same_class """


def is_same_class(obj, a_class):
    """checking the type of obj"""
    if(type(obj) == a_class):
        """Return True if it is exacly the same type"""
        return True
    else:
        """otherwise it return False"""
        return False
