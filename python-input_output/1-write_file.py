#!/usr/bin/python3
"""
writes a string to a text file (UTF8) and
returns the number of characters written:
"""


def write_file(filename="", text=""):
    """
    writes a string to a text file, returns chars
    """
    with open(filename, mode="w", encoding="utf-8") as my_file:
        return my_file.write(text)
