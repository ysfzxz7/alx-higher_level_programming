#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # copie the real list
    copied = my_list[:]
    if copied is None:
        return
    if idx < 0 or idx > len(my_list) - 1:
        return copied
    copied[idx] = element
    return copied
