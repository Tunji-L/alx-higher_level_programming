#!/usr/bin/python3
"""A class that inherit from 
class list and add to the method
"""


class MyList(list):
    """This class inherit from class
    list
    """
    def __init__(self):
        super().__init__(self)


    def print_sorted(self):
        """
        print sorted list
        """
        output = sorted(self)
        print(output)
