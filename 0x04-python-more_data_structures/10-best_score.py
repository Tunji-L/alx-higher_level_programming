#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        keys_list = list(a_dictionary.keys())
        values_list = list(a_dictionary.values())
        max_key = values_list.index(max(values_list))
        return keys_list[max_key]
    else:
        return None
