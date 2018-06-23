"""
Sudoku solver for easy and medium level of difficult.
"""
__author__ = "luis m."

from sudoku import Sudoku

if __name__ == '__main__':
    board_easy =  [[-1, -1, -1, -1,  2, -1,  4,  7, -1],
                   [-1,  2,  9,  5, -1,  4,  8, -1, -1],
                   [-1,  4, -1,  8,  7, -1, -1, -1,  9],
                   [-1,  5, -1,  9,  8, -1, -1,  6, -1],
                   [-1, -1,  6,  7, -1,  2,  5,  -1, -1],
                   [-1,  8, -1, -1,  4,  5, -1,  9, -1],
                   [ 6, -1, -1, -1,  5,  1, -1,  2, -1],
                   [-1, -1,  2,  4, -1,  8,  6,  3, -1],
                   [-1,  9,  8,  -1,  6, -1, -1, -1, -1]]
    s = Sudoku(board_easy)
    s.solver()

    board_medium = [[8,  9,  1,  -1,  2,  -1,  6,  7,  4],
                    [4, -1, -1,  -1,  1,   8,  5, -1, -1],
                    [-1, 7, -1,  -1,  6,  -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1,   6,  3,  4, -1],
                    [6, -1, -1, -1, -1, -1, -1, -1, 9],
                    [-1, 1, 8, 9, -1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, 5, -1, -1, 8, -1],
                    [-1, -1, 5, 8, 7, -1, -1, -1, 1],
                    [1, 8, 6, -1, 9, -1, 7, 2, 5]]

    s = Sudoku(board_medium)
    s.solver()

    board_hard = [[2, -1, -1, 4, -1, 6, -1, 7, -1],
                    [-1, -1, 4, -1, -1, 2, -1, -1, -1],
                    [1, 5, -1, 9, 7, -1, -1, -1, -1],
                    [-1, 3, -1, -1, 6, -1, 4, -1, -1],
                    [7, -1, 1, -1, 4, -1, 9, -1, 3],
                    [-1, -1, 8, -1, 9, -1, -1, 1, -1],
                    [-1, -1, -1, -1, 5, 4, -1, 2, 9],
                    [-1, -1, -1, 7, -1, -1, 8, -1, -1],
                    [-1, 2, -1, 6, -1, 9, -1, -1, 1]]

    s = Sudoku(board_hard)
    s.solver()

