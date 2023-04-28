#!/usr/bin/python3
"""creates a class Square"""


class Square:
    """defines class with private instance
    attributes size and position and public instance methods"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return(self.__size)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return(self.__position)

    @position.setter
    def position(self, value):
        check = 0
        while 1:
            if type(value) is not tuple or len(value) is not 2:
                check += 1
                break
