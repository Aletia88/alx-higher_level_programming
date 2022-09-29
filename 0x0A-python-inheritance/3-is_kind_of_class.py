#!/usr/bin/python3
"""defining a function is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """checking the type of obj"""
    if(type(obj) == a_class):
        """if the type of obj is exactly the same the function returns True"""
        return True
    elif(isinstance(obj, a_class)):
        """if if the obj is an instance of a class it retruns True"""
        return True
    else:
        """otherwise it retrun False"""
        return False

