#!/usr/bin/python3

for l in range(10):
    for r in range(10):
        if l < r:
            print("{}{}".format(l, r), end="")
            print("{}".format("\n" if l == 8 and r == 9 else ", "), end="")
            

