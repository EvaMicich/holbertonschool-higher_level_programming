#!/usr/bin/python3
""" square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ square class inherits from retangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """instantiate square object"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns string describing the rectangle"""
        return (
            f"[Square] ({self.id}) {self.x}/{self.y} -"
            f"{self.height}"
            )
