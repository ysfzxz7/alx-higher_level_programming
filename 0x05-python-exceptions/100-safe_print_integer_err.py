#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        print("Exception: {}".format(e))
        return False


if (__name__ == "__main__"):
    safe_function()
