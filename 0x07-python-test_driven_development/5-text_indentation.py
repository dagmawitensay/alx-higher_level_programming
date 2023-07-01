#!/usr/bin/python3
"""
    Defines a function that prints a text with 2
    new lines after each of a specified character.
"""


def text_indentation(text):
    """
        Prints text with 2 new lines after each of
        these characters '.' '?' and ':'

        param: text(str) - the text to be searched for characters
    """
    if type(text) != str:
        raise TypeError("text must be a string")

    x = 0
    while x < len(text) and text[x] == " ":
        x += 1

    while x < len(text):
        print(text[x], end='')
        if text[x] == "\n" or text[x] in ".?:":
            if text[x] in ".?:":
                print("\n")
            x += 1
            while x < len(text) and text[x] == " ":
                x += 1
            continue
        x += 1
