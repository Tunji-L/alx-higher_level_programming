#!/usr/bin/python3
"""
a class Rectangle that inherits from BaseGeometry (7-base_geometry.py)
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    class Rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        BaseGeometry.__init__(self)
        self.__width = BaseGeometry.integer_validator(self, "width", width)
        self.__height = BaseGeometry.integer_validator(self, "height", height)

    def __repr__(self):
        return (f"{self.__class__.__name__} {self.__width}/{self.__height}")

    def __str__(self):
        return (f"{self.__class__.__name__} {self.__width}/{self.__height}")

    def area(self):
        """
        area of rectangle is (lenght x width)
        """
        return (self.__width * self.__height)
