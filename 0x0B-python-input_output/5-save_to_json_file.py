#!/usr/bin/python3
"""
Module contains method that writes object to a file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    writes object to a file
    Args:
        my_ogj: object to be written
        fiilename: name of the file
    """
    with open(filename, 'w', encoding="UTF-8") as file:
        file.write(json.dumps(my_obj))
