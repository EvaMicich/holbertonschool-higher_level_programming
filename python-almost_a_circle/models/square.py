#!/usr/bin/python3
""" square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ square class inherits from retangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """instantiate square object"""
        super().__init__(size, size, x, y, id)
        self.__size = size

    def __str__(self):
        """returns string describing the rectangle"""
        return (
            f"[Square] ({self.id}) {self.x}/{self.y} - "
            f"{self.height}"
            )

    @property
    def size(self):
        """get size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """set size of square"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value
