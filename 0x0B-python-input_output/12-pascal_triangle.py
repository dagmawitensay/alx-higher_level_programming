#!/usr/bin/python3
"""
This module provides a function `pascal_triagnle`.
"""


def pascal_triangle(n):
    """
    Returns the pascall triangle.
    Args:
        n: sizes of the triang.
    """
    ans = []

    def get_triangle(row_index):
        if row_index == 0:
            return [1]
        elif row_index == 1:
            return [1, 1]
        else:
            prev_row = get_triangle(row_index - 1)
            temp = []
            for i in range(len(prev_row) - 1):
                temp.append(prev_row[i] + prev_row[i + 1])

            return [1] + temp + [1]

    for i in range(n):
        ans.append(get_triangle(i))

    return ans
