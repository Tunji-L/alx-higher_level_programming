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

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
