#!/usr/bin/python3
"""calculate the permieter of island"""


def island_perimeter(grid):
    """return perimeter of grid"""
    p = 0
    r = len(grid)
    c = len(grid[0])
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 1:
                if j == 0 or grid[i][j - 1] == 0:
                    p += 1
                if j == c - 1 or grid[i][j + 1] == 0:
                    p += 1
                if i == 0 or grid[i - 1][j] == 0:
                    p += 1
                if i == r - 1 or grid[i + 1][j] == 0:
                    p += 1
    return p
