#!/usr/bin/python3
""""
This module defines a simple functinon that
opens a file.
"""


def read_file(filename=""):
    """
    Opens a file and prints the contents of the file.
    Args:
        filename: name of the file to be opened
    """
    with open(filename, 'r', encoding="UTF-8") as file:
        data = file.read()
        print(data, end='')
