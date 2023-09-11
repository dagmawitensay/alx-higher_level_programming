#!/usr/bin/python3
"""
A module that defines a class called `square`
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        """Instantiation with size"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return s the area of the square"""
        return self.__size ** 2
