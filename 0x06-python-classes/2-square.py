#!/usr/bin/python3
"""We are defining a class for a square with
private instance attribute size.
"""


class Square:
    """This is a class with private instance
    attribute size to define a square.
    """
    def __init__(self, size):
        """Args:
            size(int): size of the square
            as a private instance attribute
        """
        self.__size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
