#!/usr/bin/python3

# function to create pascal's triangle
# n is number of rows
# check if n is <=0 and return an empty list
# create a list to hold the rows of the triangle
# r is index of element in each row
# create row with lenght r+1 uisng for loop
# m is element in each row
# update inner row element, with sum of elements above
# add completed row to triangle and return triangle


def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1] * (r + 1) for i in range(n)]

    for r in range(2, n):
        for m in range(1, r):
            triangle[r][m] = triangle[r - 1][m-1] + triangle[r - 1][m]

    return triangle
