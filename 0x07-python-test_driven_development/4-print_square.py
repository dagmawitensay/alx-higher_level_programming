#!/usr/bin/python3
"""
This module define a method print square
"""

def print_square(size):
    """
    Prints a square of given argument size
    Args:
        size: size of the square to be printed
    """
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print('#', end="")
        print()
