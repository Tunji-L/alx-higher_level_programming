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
