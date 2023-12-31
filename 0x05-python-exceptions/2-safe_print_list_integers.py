#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    printed = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            printed = printed + 1
        except (TypeError, ValueError) as e:
            continue
    print("")
    return (printed)


if (__name__ == "__main__"):
    safe_print_list_integers()
