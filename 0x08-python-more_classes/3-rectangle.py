#!/usr/bin/python3
"""writing a class that defines a rectangle
"""


class Rectangle:
    """This class defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def __str__(self):
        output = ""
        if (self.__height == 0 or self.__width == 0):
            return output
        else:
            for i in range(self.__height):
                output += ("#" * self.__width)
                if (i < (self.__height - 1)):
                    output += "\n"
            return output

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if (self.__width == 0 or self.__height == 0):
            return 0
        else:
            return ((self.__width * 2) + (self.__height * 2))
