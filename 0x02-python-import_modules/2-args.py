#!/usr/bin/python3
import sys
arg_len = len(sys.argv) - 1
if arg_len == 0:
    print(f"{arg_len} arguments.")
elif arg_len > 1:
    print(f"{arg_len} arguments:")
else:
    print(f"{arg_len} argument:")

for i in range(1, arg_len + 1):
    print(f"{i}: {sys.argv[i]}")
