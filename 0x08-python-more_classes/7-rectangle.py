#!/usr/bin/python3
"""
This module defines a Rectangle
"""


class Rectangle:
    """Rectangle class that defines a rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """int: return width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """int: return height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """print the rectangle as a form of #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        value = ""
        for i in range(self.__height):
            for j in range(self.__width):
                value += f'{self.print_symbol}'
            if i != self.__height - 1:
                value += '\n'
        return value

    def __repr__(self):
        """returns a string that is able to recreate the object"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """called when an instance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
