#!/bin/usr/python3

def safe_print_integer(value):
    success = True
    try:
        print('{}'.formar(value))
    except Exception as e:
        success = False
    return success