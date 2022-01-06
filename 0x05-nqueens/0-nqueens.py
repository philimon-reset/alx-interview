#!/usr/bin/python3

import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isnumeric():
    print("N must be a number")
    exit(1)

N = queens = int(sys.argv[1])
if N < 4:
    print("N must be at least 4")
    exit(1)


def CrossOut(g, cell, dimension):
    Grid = [x[:] for x in g]
    Grid[cell[0]][cell[1]] = 1

    # Horizontal
    for i in range(dimension):
        if Grid[cell[0]][i] != 1:
            Grid[cell[0]][i] = -1

    # Vertical
    for j in range(dimension):
        if Grid[j][cell[1]] != 1:
            Grid[j][cell[1]] = -1

    # Right Diagonal
    if cell[1] < dimension - 1:
        for x in range(1, dimension - cell[1]):
            try:
                Grid[cell[0] + x][cell[1] + x] = -1
            except BaseException:
                pass
            try:
                if cell[0] - x >= 0:
                    Grid[cell[0] - x][cell[1] + x] = -1
            except BaseException:
                pass

    # Left Diagonal
    if cell[1] > 0:
        for x in range(1, cell[1] + 1):
            try:
                if cell[1] - x >= 0:
                    Grid[cell[0] + x][cell[1] - x] = -1
            except BaseException:
                pass
            try:
                if (cell[0] - x >= 0) and (cell[1] - x >= 0):
                    Grid[cell[0] - x][cell[1] - x] = -1
            except BaseException:
                pass

    return Grid


def CountSpots(grid, dimension):
    count = 0
    for i in range(dimension):
        for j in range(dimension):
            if grid[i][j] == 0:
                count += 1
    return count


def get_answer(grid, dimension):
    spots = []
    for i in range(dimension):
        for j in range(dimension):
            if grid[i][j] == 1:
                spots.append([i, j])
    return spots


def solve(grid, row, col, dimension, queens):
    attempt = CrossOut(grid, [row, col], dimension)
    i = row + 1
    queens -= 1
    if i < dimension and CountSpots(grid, dimension) > queens:
        for j in range(dimension):
            if attempt[i][j] == 0:
                solve(attempt, i, j, dimension, queens)
    spots = get_answer(attempt, dimension)
    if len(spots) == dimension:
        print(spots)


initial_grid = [[0] * N for i in range(N)]
for col in range(N):
    solve(initial_grid, 0, col, N, N)
