#!/usr/bin/python3
""" N queens interview """

import sys

board = {}

def make_board(dimension):
    """ Generate board based on dimensions """
    for row in range(0, dimension):
        for column in range(0, dimension):
            placement = (row, column)
            board[placement] = "#"
    return board


def printing_board(dimension):
    """ function to print the board """
    i = 0
    for keys, values in board.items():
        if i % dimension == 0 and i != 0:
            print()
        i += 1
        print(f"| {values} |", end="")

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        dimension = int(sys.argv[1])
        if dimension < 4:
            print("N must be at least 4")
            exit(1)
        safe = []
        for y in range(0, dimension):
            initial = (0, dimension)
            search_board(dimension, safe, initial)
    except Exception as E:
        print("N must be a number", E)
        exit(1)


def validate(dimension):
    """ validate the placement """
    if len([i for i in board.values() if i == "#"]) < dimension and len([i for i in board.values() if i == 0]) != dimension:
        return False
    return True

def search_board(dimension, safe, inital):
    """ backtracker """
    current = fill_block(dimension, inital)
    if current:
        for i in current:
            if validate(dimension):
                if search_board(dimension, safe, i):
                    safe.append(i)
                
            else:
                return False
    if len([i for i in board.values() if i == 0]) == dimension:
        print(safe)
        return True






















def fill_block(dimension, index):
    """ function to fill queens available spots """
    board[index] = 0
# -------------------------------------------
    diagonal_C_neg_x = []
    diagonal_C_pos_x = []
    diagonal_C_neg_y = []
    diagonal_C_pos_y= []
    x = index[1]
    while x - 1 >= 0:
        less_x = (index[0], x - 1)
        diagonal_C_neg_x.append(x - 1)
        if board.get(less_x) == 0:
            return False
        board[less_x] = 1
        x -= 1

    y = index[0]
    while y - 1 >= 0:
        less_y = (y - 1, index[1])
        diagonal_C_neg_y.append(y - 1)
        if board.get(less_y) == 0:
            return False
        board[less_y] = 1
        y -= 1

    x = index[1]
    while x + 1 < dimension:
        more_x = (index[0], x + 1)
        diagonal_C_pos_x.append(x + 1)
        if board.get(more_x) == 0:
            return False
        board[more_x] = 1
        x += 1

    y = index[0]
    while y + 1 < dimension:
        more_y = (y + 1, index[1])
        diagonal_C_pos_y.append(y + 1)
        if board.get(more_y) == 0:
            return False
        board[more_y] = 1
        y += 1

    upper_left = tuple(zip(diagonal_C_pos_y, diagonal_C_neg_x))
    upper_right = tuple(zip(diagonal_C_pos_y, diagonal_C_pos_x))
    lower_left = tuple(zip(diagonal_C_neg_y, diagonal_C_neg_x))
    lower_right = tuple(zip(diagonal_C_neg_y, diagonal_C_pos_x))
    for ind in (upper_left + upper_right + lower_left + lower_right):
        if board.get(ind) == 0:
            return False
        board[ind] = 1
    return [i for i in board.keys() if board[i] == "#"]


if __name__ == '__main__':
    main()