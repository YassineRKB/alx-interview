#!/usr/bin/python3
"""module for n queens"""
import sys


def is_safe(board, row, col, N):
    """Check if a queen can be placed on board"""
    for i in range(row):
        if board[i][col] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False
    return True


def solve_n_queens_util(board, row, N, solutions):
    """Solve n queens problem using backtracking"""
    if row == N:
        solution = [''.join(map(str, row)) for row in board]
        solutions.append(solution)
        return
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solve_n_queens_util(board, row + 1, N, solutions)
            board[row][col] = 0


def solve_n_queens(N):
    """Solve n queens problem and print the solutions"""
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [[0] * N for _ in range(N)]
    solutions = []
    solve_n_queens_util(board, 0, N, solutions)
    for solution in solutions:
        queens_positions = []
        for i in range(N):
            for j in range(N):
                if solution[i][j] == '1':
                    queens_positions.append([i, j])
        print(queens_positions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    solve_n_queens(N)
