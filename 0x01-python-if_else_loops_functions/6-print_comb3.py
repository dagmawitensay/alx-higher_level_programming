#!/usr/bin/bash

for i in range(10):
    for j in range(10):
        if i >= j:
            continue
        elif i == 8 and j == 9:
            print("{}{}".format(i, j))
        else:
            print("{}{}, ".format(i, j), end="")
