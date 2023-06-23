#!/usr/bin/python3
"""
appends a string at the end of a text file (UTF8) and
returns the number of characters added:
"""


def append_write(filename="", text=""):
    """
    appends a string to a text file, returns chars
    """
    with open(filename, mode="a", encoding="utf-8") as my_file:
        return my_file.write(text)
