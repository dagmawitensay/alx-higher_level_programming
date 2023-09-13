#!/usr/bin/python3
"""
This module provides a function `write_file`.
"""


def write_file(filename="", text=""):
    """
    Writes a given text to a file with given name.
    Args:
        filename: name of the file
        text: content of the file to be written
    """
    with open(filename, 'w') as file:
        file.write(text)

    return len(text)
