#!/usr/bin/python3
"""2d matrix rotation"""


def rotate_2d_matrix(matrix):
    """rotate 2d matrix"""
    lin = len(matrix)
    for i in range(lin // 2):
        for j in range(i, lin - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[lin - 1 - j][i]
            matrix[lin - 1 - j][i] = matrix[lin - 1 - i][lin - 1 - j]
            matrix[lin - 1 - i][lin - 1 - j] = matrix[j][lin - 1 - i]
            matrix[j][lin - 1 - i] = temp
    return matrix


if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    rotate_2d_matrix(matrix)
    for row in matrix:
        print(row)
