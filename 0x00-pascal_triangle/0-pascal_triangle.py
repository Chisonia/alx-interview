#!/usr/bin/python3

# This module is a function to creates pascal's triangle

def pascal_triangle_recursive(n):
    #This function creates a paschal triangle
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
