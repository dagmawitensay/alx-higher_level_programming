#!/usr/bin/python3
"""
This moudle defines text_indentation function
"""


def text_indentation(text):
    """
    prints input text separting with ., ? and : on 
    two new lines
    Args:
        text: input string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] not in ".?:":
            if i != 0 and text[i - 1] in ".?:" and text[i] == " ":
                continue
            print(text[i], end="")
        else:
            print(text[i])
            print()
