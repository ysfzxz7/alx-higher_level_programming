#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copied = my_list[:]
    if copied is None:
        return
    if idx < 0 and idx > len(my_list) - 1:
        return copied
    copied[idx] = element
    return copied
