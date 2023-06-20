#!/usr/bin/python3
"""module tests for object in a class"""


def inherits_from(obj, a_class):
    """
    method to check if object is in a_class or inherited

    obj: object
    a_class: class to check
    """
    if type(obj) == a_class:
        return False
    else:
        return isinstance(obj, a_class)
