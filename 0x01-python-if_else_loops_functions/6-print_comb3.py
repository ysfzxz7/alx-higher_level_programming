#!/usr/bin/python3

for left in range(10):
    for right in range(10):
        if left < right:
            print("{}{}".format(left, right), end="")
            print("{}".format("\n" if left == 8 and right == 9 else ", "), end="")
