#!/usr/bin/python3
"""
This is "101-matrix-mul" module.
This module suplies one function, matrix_mul(m_a, m_b):
"""


def matrix_mul(m_a, m_b):
    """Return the muliplication of two matrix"""
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")

    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    if not is_list_of_lists(m_a):
        raise TypeError("m_a must be a list of lists")

    if not is_list_of_lists(m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")

    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    
    if not isRectangle(m_a):
        raise TypeError("each row of m_a must be of the same size")

    if not isRectangle(m_b):
        raise TypeError("each row of m_b must be of the same size")

    if not checkValues(m_a):
        raise TypeError("m_a should contain only integers or floats")

    if not checkValues(m_b):
        raise TypeError("m_b should contain only integers or floats")


    row1, col1 = len(m_a), len(m_a[0])
    row2, col2 = len(m_b), len(m_b[0])
    if col1 != row2:
        raise ValueError("m_a and m_b can't be multiplied")
    
    ans = [[0 for i in range(col2)] for j in range(row1)]
    for i in range(row1):
        for j in range(col2):
            curr_sum = 0
            for k in range(col2):
                temp = m_a[i][k] * m_b[k][j]
                curr_sum += temp
            ans[i][j] = curr_sum

    return ans

def is_list_of_lists(variable):
    return isinstance(variable, list) and all(isinstance(item, list) for item in variable)

def checkValues(matrix):
    """Check if the matrix contains integer and floats only"""
    n, m = len(matrix), len(matrix[0])
    for i in range(n):
        for j in range(m):
            value_type  = type(matrix[i][j])
            if value_type not in [float, int]:
                return False

    return True

def isRectangle(matrix):
    """Check if matrix is a rectagle, if all rows are the same length"""
    n, m = len(matrix), len(matrix[0])

    for i in range(n):
        if len(matrix[i]) != m:
            return False
 
    return True
