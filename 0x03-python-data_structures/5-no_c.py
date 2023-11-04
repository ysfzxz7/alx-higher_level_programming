#!/usr/bin/python3


def no_c(my_string):
    n_str = ""
    for i in my_string:
        if ord(i) == 99 or ord(i) == 67:
            continue
        else:
            n_str += i
    return n_str
