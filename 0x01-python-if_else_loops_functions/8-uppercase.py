#!/usr/bin/python3

def uppercase(str):
    for char in str:
        if char == str[-1]:
            print("{}".format(char))
        else:
            print("{}".format(chr(ord(char) + 32) if ord(char) in range(97, 123) else char), end="")
