#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {}
    keys_list = list(a_dictionary.keys())
    for key in keys_list:
        new_dictionary[key] = a_dictionary[key] * 2
    return new_dictionary
