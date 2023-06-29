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

    @classmethod
    def create(cls, **dictionary):
        """creates an instance from a dictionary"""
        if cls.__name__ == "Rectangle":
            instance = cls(1, 1)
        else:
            instance = cls(1)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """
        returns a python list of instances
        retireved from a json file named after its class
        """
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, 'r') as f:
                json_str = f.read()
        except:
            return []
        python_list = []
        instance_dict_list = cls.from_json_string(json_str)
        for instance_dict in instance_dict_list:
            python_list.append(cls.create(**instance_dict))
        return python_list
