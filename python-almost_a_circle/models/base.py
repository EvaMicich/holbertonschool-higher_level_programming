#!/usr/bin/python3
"""bass class"""


class Base():
    """bass class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiate bass class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id =  Base.__nb_objects
