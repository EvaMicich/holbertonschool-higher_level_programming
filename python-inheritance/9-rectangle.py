#!/usr/bin/python3
"""module for rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
bg = BaseGeometry()


class Rectangle(BaseGeometry):
    """rectangle class inherits BaseGeometry"""
    def __init__(self, width, height):
        bg.integer_validator("width", width)
        bg.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        return self.__width * self.__height
