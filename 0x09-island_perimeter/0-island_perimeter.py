#!/usr/bin/python3
'''Calculate perimeter module'''


def island_perimeter(grid):
    """
    Calculate the perimeter of the island in a 2D grid.

    Args:
        grid (list of list of int): A 2D list where 1
        represents land and 0 represents water.

    Returns:
        int: The perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:  # Land cell
                # Check the four sides
                if r == 0 or grid[r-1][c] == 0:  # Top
                    perimeter += 1
                if r == rows-1 or grid[r+1][c] == 0:  # Bottom
                    perimeter += 1
                if c == 0 or grid[r][c-1] == 0:  # Left
                    perimeter += 1
                if c == cols-1 or grid[r][c+1] == 0:  # Right
                    perimeter += 1

    return perimeter
