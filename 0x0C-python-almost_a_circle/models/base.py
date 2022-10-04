#!/usr/bin/python3
"""define a class Base"""


class Base:
    __nb_objects = 0
    """ initializing a class constructor"""


    def __init__(self, id=None):
        if(id != None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
