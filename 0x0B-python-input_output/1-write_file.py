#!/usr/bin/python3
"""
A module that defines a function that writes to a file
"""


def write_file(filename="", text=""):
    """
    Writes text to file and creates file if it doesn't exist
    Args:
        filename: name of the file
        text: data to be writen to the file
    Return:
        length of text written
    """
    with open(filename, 'w', encoding="UTF-8") as file:
        data = file.write(text)
    return data
