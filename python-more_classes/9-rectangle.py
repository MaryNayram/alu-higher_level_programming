#!/usr/bin/python3
"""creates a class Rectangle"""


class Rectangle:
    """defines class Rectangle with private instance attributes width/height
and public instance methods"""

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
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return (self.width * self.height)

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return ((2 * self.width) + (2 * self.height))

    def __str__(self):
        rec_string = ""
        if self.width == 0 or self.height == 0:
            return (rec_string)
        for row in range(self.height):
            for column in range(self.width):
                rec_string += str(self.print_symbol)
            rec_string += "\n"
        rec_string = rec_string[:-1]
        return (rec_string)

    def __repr__(self):
        rec_str = "Rectangle(%s, %s)" % (self.width, self.height)
        return (rec_str)

    def __del__(self):
        """prints goodbye message when rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not rect_1:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not rect_2:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return (rect_2)
        else:
            return (rect_1)

    @classmethod
    def square(cls, size=0):
        return (cls(size, size))
