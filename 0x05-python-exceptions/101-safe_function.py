#!/usr/bin/python3

def safe_function(fct, *args):
    returnME = None
    try:
        sum = fct(args[0], args[1])
        return sum
    except Exception as e:
        print("Exception: {}".format(e))
        return returnME


if (__name__ == "__main__"):
    safe_function()
