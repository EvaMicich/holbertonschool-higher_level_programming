#!/usr/bin/python3
"""
Square class example
"""


class Square:
    """
    A square initialised with a size as private, error messages incl
    """
    def __init__(self, size=0):
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
