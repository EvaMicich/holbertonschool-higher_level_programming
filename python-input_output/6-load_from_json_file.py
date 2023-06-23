#!/usr/bin/python3
"""creates an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """
    creates an Object from a JSON file
    """
    with open(filename, encoding="utf-8") as obj_from_json:
        return(json.load(obj_from_json))
