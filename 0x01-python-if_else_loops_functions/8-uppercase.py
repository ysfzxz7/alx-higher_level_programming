#!/usr/bin/python3

def uppercase(str):
    for i in str:
        n = ord(i)
        char = chr(n - 32) if n in range(97, 123) else i
        print("{}".format(char), end="")
    print()
