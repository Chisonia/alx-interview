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
def pascal_triangle_recursive(n):
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    
    # Generate the triangle recursively for n-1 rows
    triangle = pascal_triangle_recursive(n - 1)
    
    # Create the new row based on the last row of the triangle
    last_row = triangle[-1]
    new_row = [1] + [last_row[i - 1] + last_row[i] for i in range(1, len(last_row))] + [1]
    
    return triangle + [new_row]
