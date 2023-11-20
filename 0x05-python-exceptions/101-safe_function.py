#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    returnME = None
    try:
        sum = fct(*args)
        return sum
    except Exception as e:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return returnME


if (__name__ == "__main__"):
    safe_function()
