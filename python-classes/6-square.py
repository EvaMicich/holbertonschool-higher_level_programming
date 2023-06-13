#!/usr/bin/python3
"""
Square class example
"""


class Square:
    """
    A square initialised with a size and position
    """

    def __init__(self, size=0, position=(0, 0)):
        """initalise square"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """get size"""
        return self.__size

    @property
    def position(self):
        """get position"""
        return self.__position

    @size.setter
    def size(self, size):
        """set size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @position.setter
    def position(self, position):
        """set position"""
        error_message = "position must be a tuple of 2 positive integers"
        if type(position) != tuple or len(position) != 2:
            raise TypeError(error_message)
        for value in position:
            if type(value) != int or value < 0:
                raise TypeError(error_message)
        self.__position = position

    def area(self):
        """return square area"""
        return self.__size ** 2

    def my_print(self):
        """print sqaure"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.position[1]):
                print("")
            for i in range(self.size):
                print(" " * self.position[0], end="")
                print("#" * self.size)
