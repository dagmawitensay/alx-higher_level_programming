#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for item in matrix:
        for value in item:
            print("{:d}".format(value), end=" ")
        print()

