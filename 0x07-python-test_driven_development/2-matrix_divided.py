#!/usr/bin/python3
"""
This module defines a function  matrix_divided
"""


def matrix_divided(matrix, div):
    """
    Accepts a matrix and returns a new matrix with elements divided
    by given value div
    Args:
        matrix: input matrix
        div: value to divide elements of the matrix

    Return:
        new matrix with elemnts of input matrix devided by div
    """
    if matrix == [[]]:
        return matrix
    row_len = len(matrix[0])
    result = []
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        temp = []
        for i in row:
            if type(i) not in [int, float]:
                raise TypeError(\
                        "matrix must be a matrix (list of lists) of integers/floats")
            temp.append(round(i / div, 2))
        result.append(temp)

    return result
