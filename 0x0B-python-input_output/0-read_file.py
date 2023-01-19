#/usr/bin/python3
""" define a function that reads a text file"""


def read_file(filename=""):
    """ opeining the txt file"""
    with open(filename, encoding='utf-8') as read_file:
        for line in read_file:
            print(line, end="")
