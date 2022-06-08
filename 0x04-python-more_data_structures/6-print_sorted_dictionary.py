#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a_dictionary1 = {}
    keys_list = list(a_dictionary.keys())
    keys_list.sort()
    for i in keys_list:
      a_dictionary1.update({i:a_dictionary.get(i)})
    for i,j in a_dictionary1.items():
      print("{} : {}".format(i, j))
    return a_dictionary1
