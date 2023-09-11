#!/usr/bin/python3
"""This class provides a class called MyList"""

class MyList(list):
    """
    MyList is a subclass of list that provides additional functionality.

    Public Methods:
        print_sorted(): Print the list in ascending order.
    """
    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
