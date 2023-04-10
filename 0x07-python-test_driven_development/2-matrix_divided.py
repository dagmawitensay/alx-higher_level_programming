#!/usr/bin/python3
def matrix_divided(matrix, div):
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
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            temp.append(round(i / div, 2))
        result.append(temp)

    return result
