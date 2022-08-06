#!/usr/bin/python3
"""
A class Student that defines a student
"""


class Student:
    """
    A class Student that defines a student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None:
            dictionary = {}
            keys = list(self.__dict__.keys())
            for i in keys:
                if i in attrs:
                    dictionary.update({i: self.__dict__[i]})
            return dictionary
        else:
            return self.__dict__
