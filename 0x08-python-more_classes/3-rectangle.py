#!/usr/bin/python3
"""
rectangle class
"""


class Rectangle:
    """
    class rectangle
    """

    def __init__(self, width=0, height=0):
        """ __Init__ rectangles """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        width getter
        Returns width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        def width setter
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

    def area(self):
        """
        area getter
        Returns area of rectangle
        """
        return (self.__height * self.__width)

    def perimeter(self):
        """
        perimeter getter
        Returns the perimeter of rectangle, if width or height is equals
        0 returns 0
        """
        if (self.__width == 0 or self.__height == 0):
            return (0)

        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """
        rectangle as string with # symbol
        Returns the rectange as string with symbols #
        """
        result = ""

        if (self.__width == 0 or self.__height == 0):
            return (result)

        for i in range(self.__height):
            result += (self.__width * "#") + "\n"

        return (result[:-1])
