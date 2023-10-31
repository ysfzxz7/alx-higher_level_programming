#!/usr/bin/python3

for x in range(10):
    for i in range(10):
        if x < i:
            print("{}{}".format(x, i), end="")
            print("{}".format("\n" if x == 8 and i == 9 else ", "), end="")
