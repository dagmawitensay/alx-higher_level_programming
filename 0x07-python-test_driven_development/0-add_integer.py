#!/usr/bin/python3
"""
This module defines a simple method
to add to given numbers
"""


def add_integer(a, b=98):
    """
    Returns a + b
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError(" b must be an integer")
    if type(a) is not int:
        a = int(a)
    if type(b) is not int:
        b = int(b)

    return a + b
