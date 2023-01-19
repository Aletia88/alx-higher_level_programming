#!/usr/bin/python3
"""define a function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """ appends a string at the end of a text file """
    with open(filename, mode='a', encoding='utf-8') as a:
        return a.write(text)
