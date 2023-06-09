#!/usr/bin/python3
"""rectangle class"""
from models.base import Base
import json


class Rectangle(Base):
    """rectangle class inheriting from base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """instatiate the rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """get width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width of rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height of rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get x of rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """set x of rectangle"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get y of rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """set y of rectangle"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints the rectange with # symbol"""
        if self.width == 0 or self.height == 0:
            return ""
        rectangle_str = ""
        for num in range(self.y):
            print("")
        for i in range(self.height):
            rectangle_str += " " * self.x
            for j in range(self.width):
                rectangle_str += str("#")
            if i != self.height - 1:
                rectangle_str += "\n"
        print(rectangle_str)

    def __str__(self):
        """returns string describing the rectangle"""
        return (
            f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
            f"{self.width}/{self.height}"
            )

    def update(self, *args, **kwargs):
        """updates values in te rectangle"""
        att_list = ["id", "width", "height", "x", "y"]
        for arg in args:
            try:
                setattr(self, att_list[args.index(arg)], arg)
            except:
                pass
        for key in kwargs:
            try:
                setattr(self, key, kwargs[key])
            except:
                pass

    def to_dictionary(self):
        "makes dictionary format of rectangle """
        att_dict = {}
        key_list = ["x", "y", "id", "height", "width"]
        for key in key_list:
            att_dict[key] = getattr(self, key)
        return att_dict
