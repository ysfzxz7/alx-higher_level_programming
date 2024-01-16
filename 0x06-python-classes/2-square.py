#!/usr/bin/python3
"""respresention of class Square """


class Square:
    """
    This is an exemple of class ..
    """
    def __init__(self, size=0):
        if (type(size)) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size