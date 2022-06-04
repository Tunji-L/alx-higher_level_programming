#!/usr/bin/python3
def no_c(my_string):
    str_list = []
    for i in my_string:
        if i == 'c' or i == 'C':
            continue
        else:
            str_list.append(i)

    my_string = ''.join(str_list)
    return my_string
