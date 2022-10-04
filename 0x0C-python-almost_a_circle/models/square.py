#!/usr/bin/python3

from models.rectangle import Rectangle
""" class Square that inherits from Rectangle"""


class Square(Rectangle):
    """ initializing a function"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return '[Square] ({}) {}/{} - {}'.format(self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """get size"""
        return self.width

    @size.setter
    def size(self, value):
        """set size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if len(args) != 0:
            index = 0
            for arg in args:
                if index == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    self.id = arg
                elif index == 1:
                    self.size = arg
                elif index == 2:
                    self.x = arg
                elif index == 3:
                    self.y = arg
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
    def to_dictionary(self):
        """A dictionary representation of a Square"""
        dic ={
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y":self.y
            }
        return dic
