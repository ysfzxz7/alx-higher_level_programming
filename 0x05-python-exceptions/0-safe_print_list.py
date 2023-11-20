#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    printed = 0
    for i in my_list:
        try:
            print("{}".format(i), end="")
            printed = printed + 1
        except:
            pass
    print("")
    return printed