#!/usr/bin/python3

def uppercase(str):
    output = ""
    for char in str:
        if char == str[-1]:
            output += "{}".format(chr(ord(char) - 32))
        else:
            output += "{}".format(chr(ord(char) - 32) if ord(char) in range(97, 123) else char)
    print(output)
