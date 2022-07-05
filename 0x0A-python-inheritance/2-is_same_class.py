#!/usr/bin/python3
"""
Function that returns True if the object is exactly
an instance of the specified class ; otherwise False.
"""


def is_same_class(obj, a_class):
    """Function that return true or false if obj
    type is exactly the a_class

    Args:
        obj: object to check
        a_class: class to check on

    Return:
        True: if obj type is a_class
        False: if obj type is not a_class
    """
    return type(obj) is  a_class
