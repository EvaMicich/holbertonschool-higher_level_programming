#!/usr/bin/python3
""" class Student that defines a student"""


class Student:
    """
    class for a student
    arguments:
    first_name
    last_name
    age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        new_dict = {}
        if attrs is None:
            return vars(self)
        else:
            for attribute in attrs:
                if hasattr(self, attribute):
                    new_dict[attribute] = getattr(self, attribute)
            return new_dict

    def reload_from_json(self, json):
        """
        replaces all attributes of the Student instance
        """
        for key, value in json.items():
            setattr(self, key, value)
