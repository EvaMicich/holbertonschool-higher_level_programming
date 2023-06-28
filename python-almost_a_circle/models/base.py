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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns list on dictionaries in json format"""
        if list_dictionaries is None or list_dictionaries == []:
            return f"[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = f"{cls.__name__}.json"
        if list_objs is None:
            list_objs = []
        json_string = cls.to_json_string(
            [obj.to_dictionary() for obj in list_objs]
            )
        with open(filename, 'w', encoding="utf-8") as new_file:
            new_file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string:"""
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)
