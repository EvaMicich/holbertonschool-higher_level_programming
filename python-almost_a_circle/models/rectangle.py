#!/usr/bin/python3
"""rectangle class"""
from models.base import Base


class Rectangle(Base):
    """rectangle class inheriting from base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """instatiate the rectangle"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """get width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width of rectangle"""
        self.__width = value

    @property
    def height(self):
        """get height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height of rectangle"""
        self.__height = value

    @property
    def x(self):
        """get x of rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """set x of rectangle"""
        self.__x = value

    @property
    def y(self):
        """get y of rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """set y of rectangle"""
        self.__y = value
