#!/usr/bin/python3
"""
This module provides a function `append_after`.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Appends the given text to the filename with new string
    at each line.
    Args:
        filename: name of the fle.
        search_string: string to be searched.
        new_string: string to be appended at end.
    """
    with open(filename) as file:
        data = file.readlines()

    with open(filename, 'w') as file:
        for line in data:
            if line.find(search_string) != -1:
                file.write(line)
                file.write(new_string)
            else:
                file.write(line)
