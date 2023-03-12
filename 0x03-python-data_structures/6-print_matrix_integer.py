#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
    else:
        for item in matrix:
            for value in item:
                print("{:d}".format(
                    value), end=" " if value != item[-1] else '\n')
