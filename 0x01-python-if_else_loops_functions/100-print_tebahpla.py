#!/usr/bin/python3

i = 90
while i > 64:
    if i % 2 != 0:
        print("{}".format(chr(i)), end="")
    else:
        print("{}".format(chr(i + 32)), end="")
    i -= 1
