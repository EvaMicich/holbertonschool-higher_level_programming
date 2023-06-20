# Python - Inheritance

## Description
This is a learning project about Python's Object-Oriented Programming (OOP) capabilities, focusing on the concept of inheritance.

## Files
- `0-lookup.py` : Function that returns the list of available attributes and methods of an object.
- `1-my_list.py` : Class MyList that inherits from list. Also includes tests file `tests/1-my_list.txt`
- `2-is_same_class.py` : Function that returns True if the object is exactly an instance of the specified class; otherwise False.
- `3-is_kind_of_class.py` : Function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class; otherwise False.
- `4-inherits_from.py` : Function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise False.
- `5-base_geometry.py` : Empty class BaseGeometry.
- `6-base_geometry.py` : Class BaseGeometry that raises an Exception with the message `area() is not implemented`
- `7-base_geometry.py`, `tests/7-base_geometry.txt` : Class BaseGeometry that validates value and raises an Exception with the message `area() is not implemented`
- `8-rectangle.py` : Class Rectangle that inherits from BaseGeometry.

## Usage
To execute the scripts, use:
```
./file_name.py
```

To execute the tests, use:
```
python3 -m doctest ./tests/*
```
