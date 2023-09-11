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
