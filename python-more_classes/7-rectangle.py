#!/usr/bin/python3
"""creates a class Rectangle"""


class Rectangle:
    """defines class Rectangle with private instance attributes width/height
and public instance methods to return the rectangle area and primeter
and public class attributes to track of number of instances and print symbol
and can print the rectangle using print_symbol with print() or str()
and returns representation of the rectangle to be used by eval()
and prints message when deleted"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
