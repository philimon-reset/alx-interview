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
    # if len(sys.argv) != 2:
    #     print("Usage: nqueens N")
    #     exit(1)
    try:
        dimension = 6
        # if dimension < 4:
        #     print("N must be at least 4")
        #     exit(1)
        safe = []
        total_run = []
        started = False
        spots_left = dimension
        for x in range(0, dimension):
            for y in range(0, dimension):
                if started == False:
                    board = make_board(dimension)
                    current = fill_block(dimension, (x,y), spots_left)
                    spots_left -= 1
                    if not current:
                        board = make_board(dimension)
                        spots_left = dimension
                        total_run = []
                    else:
                        total_run.extend(((x,y), current))
                        spots_left -= 1
                        started = True
                while spots_left > 0:
                    current = fill_block(dimension, current, spots_left)
                    spots_left -= 1
                    total_run.append(current)
                    print(total_run, "\n", "\n")
                    if not current:
                        board = make_board(dimension)
                        spots_left = dimension
                        total_run = []
                        break
                valid = True
                if len(total_run) > 0:
                    for i in range(len(safe)):
                        if len(set(safe[i]) - set(total_run)) != 0:
                            pass
                        else:
                            valid = False
                            break
                    if valid:
                        safe.append(total_run)
                    spots_left = dimension
                    total_run = []
                started = False
        for i in safe:
            print(i)
    except Exception as E:
        print("N must be a number", E)
        exit(1)



def fill_block(dimension, index, spots_left):
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
    if len([i for i in board.values() if i == "#"]) < spots_left and spots_left != 0:
        return False
    return [i for i in board.keys() if board[i] == "#"][0]


if __name__ == '__main__':
    main()