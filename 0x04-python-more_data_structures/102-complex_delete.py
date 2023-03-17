#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    deletable = []
    for i, j in a_dictionary.items():
        if j == value:
            deletable.append(i)
    for i in deletable:
        del a_dictionary[i]
    return a_dictionary
