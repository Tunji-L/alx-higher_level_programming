#!/usr/bin/python3
"""
writing a function that prints
My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """This function takes
    Args:
      first_name: arg firstname
      last_name: arg lastname

    and return My name is <first name> <last name>
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    message = "My name is {:s} {:s}"
    print(message.format(first_name, last_name))
