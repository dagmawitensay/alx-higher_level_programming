#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = [[item**2 for item in row] for row in matrix]
    return square_matrix
