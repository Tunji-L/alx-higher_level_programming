#!/usr/bin/python3
for i in range(100):
    if i < 10:
        print("0{}".format(str(i) + ', ' if i < 9 else str(i)), end='')
    else:
        print(", {}".format(i), end='')
print()
