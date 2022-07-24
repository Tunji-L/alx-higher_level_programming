#!/usr/bin/python3
"""Write a function that reads a text file (UTF8)
and prints it to stdout
"""


def read_file(filename=""):
    """This is a function that reads a text file (UTF8)
    and prints it to stdout
    """
    with open(filename,'r', encoding='utf8') as f:
        lines = f.read()
        print(lines, end="")
