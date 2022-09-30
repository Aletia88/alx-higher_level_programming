#!/usr/bin/python3
""" define a function that writes a string to a text file"""


def write_file(filename="", text=""):
    """open the file and write a txt"""
    with open(filename, mode='w', encoding="utf-8") as write_file:
        return write_file.write(text)
