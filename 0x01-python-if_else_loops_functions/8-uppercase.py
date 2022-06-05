#!/usr/bin/python3
def uppercase(str):
    str_list = []
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            str_list.append(chr(ord(i) - 32))
        else:
            str_list.append(i)
    str_upper = ''.join(str_list)
    print(str_upper)
