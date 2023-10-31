#!/usr/bin/python3

def remove_char_at(str, n):
    tmp = ""
    counter = 0

    for i in str:
        if counter == n:
            counter += 1
            continue
        tmp = tmp + i
        counter += 1
    return (tmp)
