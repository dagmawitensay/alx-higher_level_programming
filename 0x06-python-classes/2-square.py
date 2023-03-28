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
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
