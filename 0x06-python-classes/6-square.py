#!/usr/bin/python3
"""respresention of class Square """


class Square:
    """
    This is an exemple of class ..
    """
    def __init__(self, size=0, position=(0, 0)):
        """ init a new square
        Agrs =>:
                size (int): The size must be < 0
                position(int, int) : position of the new square
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """This methode serve a getter to the value size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """This methode serve as setter to the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >=0")
        self.__size = value

    @property
    def position(self):
        """this is a getter of the position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """This methode is a setter for the position"""
        if (not isinstance(value, tuple) or len(value) != 2
                or all(isinstance(n, int) for n in value)
                or not all(n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """This methode return the Area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """This func is used to print the a Square in Hashtag"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for x in range(self.__size):
                print("#", end="")
            print("")
