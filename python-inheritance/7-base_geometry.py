#!/usr/bin/python3
""" module to clreate class BaseGeometry"""


class BaseGeometry():
    """new basegeometry class"""

    def area(self):
        """area of the geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates integer value"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
