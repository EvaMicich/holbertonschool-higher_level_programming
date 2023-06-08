# Python - Exceptions

This repository, `python-exceptions`, contains Python scripts for understanding and handling exceptions in Python. This project is part of the curriculum of Holberton School's Higher-Level Programming track.

## Description of Repository Contents

1. **0-safe_print_list.py**: A function that prints `x` elements of a list, with exception handling for an IndexError if `x` is greater than the length of the list.
2. **1-safe_print_integer.py**: A function that prints an integer with "{:d}".format(), with exception handling for a TypeError if the input value is not an integer.
3. **2-safe_print_list_integers.py**: A function that prints the first `x` integers of a list, with exception handling for an IndexError if `x` is greater than the length of the list and a TypeError if a list element is not an integer.
4. **3-safe_print_division.py**: A function that divides 2 integers and prints the result, with exception handling for a ZeroDivisionError.
5. **4-list_division.py**: A function that divides element by element 2 lists, with exception handling for TypeErrors (if the list elements are not integers or floats), ZeroDivisionErrors, and IndexError (if the lists are too short).
6. **5-raise_exception.py**: A function that raises a TypeError exception.
7. **6-raise_exception_msg.py**: A function that raises a NameError exception with a custom message.

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

- Why Python programming is awesome
- What’s the difference between errors and exceptions
- What are exceptions and how to use them
- When do we need to use exceptions
- How to correctly handle an exception
- What’s the purpose of catching exceptions
- How to raise a builtin exception
- When do we need to implement a clean-up action after an exception

## Requirements

- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using wc

## Resources

Read or watch:

- [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Learn to Program 11 Static & Exception Handling](https://www.youtube.com/watch?v=iH4JJuoHQHc) (starting at minute 7)
