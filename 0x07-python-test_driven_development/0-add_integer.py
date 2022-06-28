#!/usr/bin/python3
"""
This function add
two integers together
"""


def add_integer(a, b=98):
    """ Function that add two integers or float
    convert float to integer before addition

    Args:
      a: first paramter (integer/float)
      b: second parameter (integer/float)

      Returns: sum of the two numbers or raises
      TypeError if condition not fulfilled
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    else:
        if isinstance(a, float):
            a = int(a)
        if isinstance(b, float):
            b = int(b)
    return (a + b)
