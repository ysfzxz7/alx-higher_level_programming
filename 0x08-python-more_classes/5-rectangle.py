#!/usr/bin/python3
"""
Create a rectangle class
"""


class Rectangle:
    """
    The class rectangle
    """

    def __init__(self, width=0, height=0):
        """ Initialize rectangles """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        The width getter
        Returns the self width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        defining the width setter
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
        The height getter
        Returns the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        The height setter
        Raise a TypeError and ValueError if soe conditions are not met
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """
        The area getter
        Returns the area of rectangle
        """
        return (self.__height * self.__width)

    def perimeter(self):
        """
        The perimeter getter
        Returns the perimeter of rectangle, if width or height is equals
        0 returns 0
        """
        if (self.__width == 0 or self.__height == 0):
            return (0)

        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """
        The rectangle as string with # symbol
        Returns the rectange as string with symbols #
        """
        result = ""

        if (self.__width == 0 or self.__height == 0):
            return (result)

        for i in range(self.__height):
            result += (self.__width * "#") + "\n"

        return (result[:-1])

    def __repr__(self):
        """Method that returns the string represantion of the instance

        Returns:
            string represenation of the object
        """

        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """
        Prints a message
        This function called when object is deleted,
        and prints 'Bye rectangle...'
        """
        print("Bye rectangle...")