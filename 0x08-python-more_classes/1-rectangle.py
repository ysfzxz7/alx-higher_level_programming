#!/usr/bin/python3
"""
rectangle class
"""


class Rectangle:
    """
    class rectangle
    """

    def __init__(self, width=0, height=0):
        """ Initialize rectangles """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        The width getter
        return the rect width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        the width setter
        Raise a TypeError and ValueError if some conditions are not met
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        height getter
        Returns height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter
        Raise a TypeError and ValueError if soe conditions are not met
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
