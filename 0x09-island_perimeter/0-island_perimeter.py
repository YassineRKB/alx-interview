#!/usr/bin/python3
"""module island_perimeter"""


def island_perimeter(g):
    """returns the perimeter of the island described in grid"""
    perimeter = 0
    if not isinstance(g, list):
        return 0
    for i, row in enumerate(g):
        if not isinstance(row, list):
            return 0
        for j, cell in enumerate(row):
            if not isinstance(cell, int):
                return 0
            if cell == 0:
                continue
            m = len(row)
            n = len(g)
            up_edge = i == 0 or (len(g[i - 1]) > j and g[i - 1][j] == 0)
            right_edge = j == m - 1 or (m > j + 1 and row[j + 1] == 0)
            down_edge = i == n - 1 or (len(g[i + 1]) > j and g[i + 1][j] == 0)
            left_edge = j == 0 or row[j - 1] == 0
            perimeter += sum((up_edge, right_edge, down_edge, left_edge))
    return perimeter
