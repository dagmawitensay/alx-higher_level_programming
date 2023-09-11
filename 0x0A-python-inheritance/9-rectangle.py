#!/usr/bin/python3
"""
This module provides a class called `Rectangle`
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    This class inherits from Base Geometry class.
    """
    def __init__(self, width, height):
        """INstantiation with widht and height"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def areat(self):
        """Caluclates and returns the area of the recntagle"""
        return self.width * self. height

    def __str__(self):
        return "[Rectangle] {:d}/{:d}".format(self.width, self.height)

    def __repr__(self):
        return "[Rectangle] {:d}/{:d}".format(self.width, self.height)

