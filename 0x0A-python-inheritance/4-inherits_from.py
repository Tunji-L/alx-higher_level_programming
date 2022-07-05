#!/usr/bin/python3
"""function that returns True if the object is an instance of
a class that inherited (directly or indirectly) from the 
specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """Function that return true or false if obj
    is an instance of a_class inherited from a 
    specified class.

    Args:
        obj: object to check
        a_class: class to check on

    Return:
        True: if obj type is an instance of class
        False: if obj type is not an instance of class
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
