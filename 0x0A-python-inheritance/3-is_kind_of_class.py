#!/usr/bin/python3
"""function that returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """Function that return true or false if obj
    is an instance of a_class or a_class superclass

    Args:
        obj: object to check
        a_class: class to check on

    Return:
        True: if obj type is an instance of class
        False: if obj type is not an instance of class
    """
    return isinstance(obj, a_class)
