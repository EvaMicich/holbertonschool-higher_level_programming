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
            f"[Square] ({self.id}) {self.x}/{self.y} - "
            f"{self.height}"
            )

    @property
    def size(self):
        """get size of square"""
        return self.width

    @size.setter
    def size(self, value):
        """set size of square"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        update the square
        args order: "id", "size", "x", "y"
        kwargs: "id=x", "size=x", "x=x", "y=x"
        """
        att_list = ["id", "size", "x", "y"]
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
