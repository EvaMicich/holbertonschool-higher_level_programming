# Python Input/Output Project

This repository contains Python code that showcases various operations related to file handling and JSON manipulation.

## Tasks and Files
0-read_file.py: A function that reads a text file (UTF8) and prints it to stdout.

1-write_file.py: A function that writes a string to a text file (UTF8) and returns the number of characters written.

2-append_write.py: A function that appends a string at the end of a text file (UTF8) and returns the number of characters added.

3-to_json_string.py: A function that returns the JSON representation of an object (string).

4-from_json_string.py: A function that returns an object (Python data structure) represented by a JSON string.

5-save_to_json_file.py: A function that writes an object to a text file, using a JSON representation.

6-load_from_json_file.py: A function that creates an object from a "JSON file".

Task 7: Load, add, save (7-add_item.py) - This task involves writing a script that accepts arguments, adds them to a Python list, and saves them to a file named add_item.json. It tests your understanding of handling command-line arguments, file operations, and JSON data manipulation.

Task 8: Class to JSON (8-class_to_json.py) - The task is about writing a function that returns a dictionary description of an object for JSON serialization. The focus here is on understanding how to translate Python class instances into a dictionary representation, and how JSON serialization works.

Task 9: Student to JSON (9-student.py) - This task requires creating a class Student that defines a student with attributes first_name, last_name, and age. A method to_json is required to retrieve a dictionary representation of the Student instance. This task tests your understanding of class representation and JSON serialization.

Task 10: Student to JSON with filter (10-student.py) - Based on task 9, this task enhances the to_json method to accept an optional attrs argument. If attrs is a list of strings, only the attribute names present in this list are retrieved. This task tests your understanding of class representation, JSON serialization, and filtering attributes.

Task 11: Student to disk and reload (11-student.py) - This task extends task 10 to include a method reload_from_json that replaces all attributes of the Student instance using a JSON dictionary. This task is about understanding JSON deserialization and the manipulation of class instance attributes.

Task 12: Pascal's Triangle (12-pascal_triangle.py) - This task requires implementing a function pascal_triangle that returns a list of lists of integers representing Pascal's Triangle of n. The challenge here lies in understanding the mathematical logic of Pascal's Triangle and implementing it programmatically.

## Learning Objectives
By the end of this project, you will be able to:

Open, write, read, and append to a file in Python
Handle the cursor in a file and ensure its closure after usage
Use with statement in Python
Understand and implement JSON serialization and deserialization
Convert a Python data structure to a JSON string and vice versa
Requirements
All Python scripts are tested on Ubuntu 20.04 LTS, using python3 (version 3.8.5)
Code follows PEP8 style (version 2.7.*)
All files are executable and end with a new line
All modules, classes, and functions have documentation.
Test Cases
All test files should be inside a folder named tests and should be text files (extension: .txt). Tests can be executed using the command: python3 -m doctest ./tests/*.
