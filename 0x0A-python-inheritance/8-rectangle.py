#!/usr/bin/python3
"""defines a class BaseGeometry"""


class BaseGeometry:
    """define a method area"""
    def area(self):
        """raise exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if(type(value) != int):
            raise TypeError("{} must be an integer".format(name))
        if(value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
""" Defines a class Rectangle that inherits from BaseGeometry."""


class Rectangle(BaseGeometry):
    """Represent a rectangle"""


    def __init__(self, width, height):
        """Intialize a new Rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
