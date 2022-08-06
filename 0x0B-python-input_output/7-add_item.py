#!/usr/bin/python3
"""
Write a script that adds all arguments to a Python list,
and then save them to a file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    function that writes an Object to a text file,
    using a JSON representation
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)


def load_from_json_file(filename):
    """
    function that creates an Object from a “JSON file”
    Args:
        filename: fule containing string
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)


if __name__ == "__main__":
    import sys
    from os.path import exists
    if exists("add_item.json"):
        content = load_from_json_file("add_item.json")
        content.extend(sys.argv[1:])
        save_to_json_file(content, "add_item.json")
    else:
        save_to_json_file(sys.argv[1:], "add_item.json")
