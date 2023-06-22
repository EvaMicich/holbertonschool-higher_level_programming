#!/usr/bin/python3
"""module for rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
bg = BaseGeometry()

class Rectangle(BaseGeometry):
    """rectangle class inherits BaseGeometry"""
    def __init__(self, width, height):
        self.__width = bg.integer_validator("width", width)
        self.__height = bg.integer_validator("height", height)
