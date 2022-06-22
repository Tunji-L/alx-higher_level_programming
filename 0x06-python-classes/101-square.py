#!/usr/bin/python3
"""We are defining a class for a square with
private instance attribute size.
"""


class Square:
    """This is a class with private instance
    attribute size to define a square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """Args:
            size(int): size of the square
            as a private instance attribute
        """
        self.size = size
        self.position = position

    def __str__(self):
        output = ""
        if self.size == 0:
            return output
        else:
            for i in range(self.position[1]):
                output += "\n"
            for i in range(0, self.size):
                for k in range(self.position[0]):
                    output += " "
                for j in range(self.size):
                    output += "#"
                if i is not (self.size - 1):
                    output += "\n"
            return output

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

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if type(value[0]) != int or type(value[1]) != int or value[0] < 0 \
                or value[1] < 0 or len(value) != 2 \
                or not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """This public instance method compute the
        square and return the result
        """
        return (self.__size ** 2)

    def my_print(self):
        """This public instance method prints the square
        shape with # sign putting position into consideration
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end='')
                for k in range(self.__size):
                    print("#", end='')
                print()
