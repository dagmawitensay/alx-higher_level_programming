#!/usr/bin/python3

"""
    This module defines a function that prints
    a firstname and a lastname
"""


def say_my_name(first_name, last_name=""):
    """
        Takes two string as input and prints them to stdout
        param: first_name(str) - the first name to print
        param: last_name(str) - the last name to print (optional)
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
