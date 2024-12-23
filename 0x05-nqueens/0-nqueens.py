#!/usr/bin/python3
'''The Queen module'''
import sys


def is_safe(row, col, board):
    """
    Check if it's safe to place a queen at the given row and column
    """
    for r in range(row):
        # Check column and diagonal conflicts
        if board[r] == col or abs(board[r] - col) == abs(r - row):
            return False
    return True


def solve_n_queens(row, board, solutions):
    """
    Recursively solve the N Queens problem using backtracking
    """
    if row == len(board):
        # If all queens are placed, add solution
        solutions.append([[i, board[i]] for i in range(len(board))])
        return

    for col in range(len(board)):
        if is_safe(row, col, board):
            # Place the queen
            board[row] = col
            # Recur to place the rest of the queens
            solve_n_queens(row + 1, board, solutions)
            # Backtrack
            board[row] = -1


def main():
    """
    Main function to handle input and output
    """
    # Check for correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the board and solutions
    board = [-1] * N
    solutions = []

    # Solve the N Queens problem
    solve_n_queens(0, board, solutions)

    # Print all solutions
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
