#!/usr/bin/python3
"""
This module provide  a function `append_write`.
"""


def append_write(filename="", text=""):
    """
    Append the given text to the end of the file with
    the given filename.
    Args:
        filename: name of the file.
        text: content to be written.
    """
    with open(filename, 'a') as file:
        file.write(text)

    return len(text)
