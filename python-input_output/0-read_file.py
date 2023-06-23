#!/usr/bin/python3
"""Reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding="utf-8") as my_file:
        read_file = my_file.read()
        print(read_file, end="")
