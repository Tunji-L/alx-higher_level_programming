#!/usr/bin/python3
"""class BaseGeometry with Public instance method: area
that raises an Exception with the message area() is not implemented
"""


class BaseGeometry:
    """class BaseGeometry with Public instance method: area
    that raises an Exception with the message area() is not implemented
    """
    def __init__(self):
        pass

    def area(self):
        """Raise Exception
        area() is not implemented
        """
        raise Exception("area() is not implemented")
