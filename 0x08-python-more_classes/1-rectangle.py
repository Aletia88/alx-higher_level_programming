#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
   """Represent a rectangle."""

    def __init__(self, width=0,height=0):
          """Initialize a new Rectangle.
                Args:
                    width (int): The width of the new rectangle.
                    height (int): The height of the new rectangle.
            """
        self.width = width
        self.height = height
 
    @property    
    def height(self):
         """Get/set the width of the rectangle."""
        return self.__height

    @width.setter
    def height(self, value):
        """set width"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property    
    def width(self):
        """Get/set the height of the rectangle."""
        return self._Rectangle__width

    @height.setter
    def width(self, value):
        """set height"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._Rectangle__width = value
