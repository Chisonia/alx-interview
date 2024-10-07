#!/usr/bin/python3

"""This module is a function to creates pascal's triangle"""


def pascal_triangle(n):
    """This function prints a paschal triangle"""
    if n <= 0:
        return []

    triangle = []
    """Initialize triangle"""

    for r in range(n):
        """ Loop to generate each row of Pascal's Triangle"""
        row = [1] * (r + 1)
        """Each row starts and ends with 1"""
        for m in range(1, r):
            """Fill in the internal values for each row"""
            row[m] = triangle[r - 1][m-1] + triangle[r - 1][m]

        triangle.append(row)
        """Add the completed row to the triangle"""

    return triangle
