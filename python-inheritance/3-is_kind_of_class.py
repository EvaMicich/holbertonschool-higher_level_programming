#!/usr/bin/python3
"""module tests for object in a class"""


def is_kind_of_class(obj, a_class):
    """
    method to check if object is in a_class or inherited

    obj: object
    a_class: class to check
    """
    return isinstance(obj, a_class)
