#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    arg_sum = 0
    for i in args:
        arg_sum += int(i)
    print(arg_sum)
