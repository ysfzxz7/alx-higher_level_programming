#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    luis = []
    for i in my_list:
        if i % 2 == 0:
            luis.append(True)
        else:
            luis.append(False)
    return luis
