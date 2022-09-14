#!/usr/bin/python3
"""define the Square class"""

class Square:
    """ """
    def __init__(self, size=0):
        """squre is initaialized"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >=0")
    def area(slef):
        self.area = size * size
