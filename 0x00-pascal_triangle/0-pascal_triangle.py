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

    triangle = []

    for r in range(n):
        row = [1] * (r + 1)

        for m in range(1, r):
            row[m] = triangle[r - 1][m-1] + triangle[r - 1][m]

        triangle.append(row)

    return triangle
