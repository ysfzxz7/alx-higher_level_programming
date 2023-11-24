#!/usr/bin/python3

def add_integer(a, b=98):
    """this add_integer func add two int together and return the sum

    Args:
        a (_int or float_): _the first number_
        b (int or float, optional): _the second number_. Defaults to 98.

    Raises:
        TypeError: _description_
        TypeError: _description_

    Returns:
        _type_: _description_
    """
    if (type(a) != int) or (type(a) != float):
        raise TypeError("a must be an integer")
    if (type(b) != int or type(b) != float):
        raise TypeError("b must be an integer") 
    return (a + b)