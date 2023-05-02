#!/usr/bin/python3
"""
This module defines a square with given size
"""


class Square:
    """
    A square class that defines a sqaare instace with
    a given size
    Args:
        size (int): size of the square
    """
    def __init__(self, size=0):
        self.size(size)

    @property
    def size(self):
        """
        getter for the attribute size
        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        returns the area of the square
        """
        return self.__size ** 2
