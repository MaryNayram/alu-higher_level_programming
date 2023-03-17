#!/usr/bin/python3
"""creates class with private instance attribute size"""


class Square:
    """creates class with  private instance attribute
and public instance method(method area) which calculates area."""

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return(self.__size * self.__size)
