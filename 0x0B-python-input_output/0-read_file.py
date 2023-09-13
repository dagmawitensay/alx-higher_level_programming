#!/usr/bin/python3
"""
This module provides a function `read_file`
"""


def read_file(filename=""):
    """
    Reads and prints the contents of a file.
    Args:
        filename: name of the file to be read.
    """
    with open(filename) as file:
        print(file.read(), end="")
