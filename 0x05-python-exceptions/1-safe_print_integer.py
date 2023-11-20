#!/bin/usr/python3

def safe_print_integer(value):
    
    try:
        print('{:d}\n'.formar(value))
        return True
    except Exception as e:
        return False
