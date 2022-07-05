#!/usr/bin/python3
"""This function returns all the available
attributes and methods in and object
"""
def lookup(obj):
    """ function that returns the list of
    all the attributes and methods of an
    object

    Args:
      obj: arg object
    """
    return dir(obj)
