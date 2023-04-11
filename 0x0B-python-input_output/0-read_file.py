#!/usr/bin/python3
""""
This module defines a simple functinon that
opens a file.
"""
def read_file(filename=""):
    """
    Opens a file and prints the contents of the file.
    """
    with open(filename, 'r') as file:
        data = file.read()
        print(data)
