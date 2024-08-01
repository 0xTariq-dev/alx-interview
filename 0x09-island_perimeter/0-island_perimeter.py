#!/usr/bin/python3
""" Island Perimeter Solution Module """


def island_perimeter(grid):
    """
    Calculates the perimeter of the island descriped by grid

    Args:
        grid (list of lists of integers): the grid that describe the island
            contains 0 (represents water) or 1 (represents land).

    Returns:
        The perimeter of the island
    """

    if type(grid) != list or len(grid) == 0:
        return 0

    land = []
    perimeter = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                land.append((row, col))
                perimeter += 4
                if (row - 1, col) in land:
                    perimeter -= 2
                if (row, col - 1) in land:
                    perimeter -= 2

    return perimeter
