#!/usr/bin/python3
"""
Module that conatins a function that appends text to a file
"""


def append_write(filename="", text=""):
    """
    Apends text to the end of the file
    Args:
        filenema: name of the file
        text: data to be written to the file
    Return:
        length of written data
    """
    with open(filename, 'a', encoding="UTF-8") as file:
        data = file.write(text)
    return data
