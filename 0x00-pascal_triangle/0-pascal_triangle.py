#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(x):
    """alians built pyramids in the shape of a triangle (with a square base),"""
    if x <= 0:
        return []

    OnePascal = [[1] * (i + 1) for i in range(x)]
    for i in range(1, x):
        for j in range(1, i):
            OnePascal[i][j] = OnePascal[i - 1][j - 1] + OnePascal[i - 1][j]
    
    return OnePascal
