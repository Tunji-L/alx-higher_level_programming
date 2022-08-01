#!/usr/bin/python3
"""
a class Square that inherits from Rectangle (9-rectangle.py)
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    class Square that inherits from Rectangle
    """
    def __init__(self, size):
        self.__size = self.integer_validator("size", size)
        Rectangle.__init__(self, self.__size, self.__size)

    def area(self):
        """
        area of a square is size^2
        """
        return super().area()
