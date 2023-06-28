#!/usr/bin/python3
"""bass class"""
import json


class Base():
    """bass class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiate bass class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """returns list on dictionaries in json format"""
        if list_dictionaries is None:
            return f"[]"
        else:
            return json.dumps(list_dictionaries)
