#!/usr/bin/python3
"""
Write a function that returns the JSON representation of an object (string):
"""
import json


def to_json_string(my_obj):
    """
    function that returns the JSON representation of an object (string)
    Args:
        my_obj: python object
    """
    return json.dumps(my_obj)
