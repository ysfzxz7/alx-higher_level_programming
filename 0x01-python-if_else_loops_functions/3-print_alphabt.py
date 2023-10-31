#!/usr/bin/python3

string = ""
for i in range(97, 123):
    if i == 101 or i == 113:
        continue
    string = string + chr(i)
print("{}".format(string), end='')
