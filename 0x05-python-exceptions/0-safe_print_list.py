#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    printed = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            printed = printed + 1
        except:
            print("")
            return printed
    print("")
    return printed
