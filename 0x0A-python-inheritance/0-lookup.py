#!/usr/bin/python3
""" define a function that returns the list of avaliable attributes and methonds"""


def lookup(obj):
    """Return a list of an object"""
    return (dir(obj))
