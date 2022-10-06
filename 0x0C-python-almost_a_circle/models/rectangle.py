#!/usr/bin/python3
from models.base import Base

"""class Rectangle"""


class Rectangle(Base):
    """initalizing """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """getter method for width"""
        return self.__width

    @property
    def height(self):
        """getter method for height"""
        return self.__height

    @property
    def x(self):
        """getter method for x"""
        return self.__x

    @property
    def y(self):
        """getter method for y"""
        return self.__y

    @width.setter
    def width(self, width):
        """width setter"""
        if(type(width) != int):
            raise TypeError("width must be an integer")
        if(width <= 0):
            raise ValueError("width must be > 0 ")
        else:
            self.__width = width

    @height.setter
    def height(self, height):
        """height setter"""
        if(type(height) != int):
            raise TypeError("height must be an integer")
        if(height <= 0):
            raise ValueError("height  must be > 0 ")
        else:
            self.__height = height

    @x.setter
    def x(self, x):
        """x setter"""
        if(type(x) != int):
            raise TypeError("x must be an integer")
        if(x < 0):
            raise ValueError("x  must be >= 0 ")
        else:
            self.__x = x

    @y.setter
    def y(self, y):
        """y setter"""
        if(type(y) != int):
            raise TypeError("y must be an integer")
        if(y < 0):
            raise ValueError("y  must be >= 0 ")
        else:
            self.__y = y

    def area(self):
        """ return area of a rectangle """
        return self.__width * self.__height

    def display(self):
        """ prints rectangle in stdout """
        for i in range(self.__height):
            for j in range(self.__width):
                print('#', end="")
            print()

    def __str__(self):
        """ updating the class rectangle """
        return f'[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}'

    def update(self, *args, **kwargs):
         """Update the Rectangle.
        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
                                                                                                **kwargs (dict): New key/value pairs of attributes.
            """
        index = 0
        if len(args) != 0:
            for arg in args:
                if index == 0:
                    self.id = arg
                elif index == 1:
                    self.__width = arg
                elif index == 2:
                    self.__height = arg
                elif index == 3:
                    self.__x = arg
                elif index == 4:
                    self.__y = arg
                index += 1
        elif len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "x":
                    self.__x = value
                elif key == "y":
                    self.y__ = value
                elif key == "width":
                    self.__width = value
                elif key == "height":
                    self.__height = value

    def to_dictionary(self):
        """a dictionary representation of a Rectangle"""
        dic = {
                "id" : self.id,
                "width" : self.width,
                "height" : self.height,
                "x" : self.x,
                "y" : self.y
            }
        return dic
