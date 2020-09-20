from Board import Board
from constants import *

class Ray:
    def __init__(self, board: Board, pos: tuple):
        self._board = board
        self._pos = pos
        self._direction = None

    def traverse(self, print_board=False):
        if 0 not in self._pos and NUM_COL - 1 != self._pos[1] and NUM_ROWS - 1 != self._pos[0]:
            return False

        if self._pos in [(0, 0), (0, NUM_COL - 1), (NUM_ROWS - 1, 0), (NUM_ROWS - 1, NUM_COL - 1)]:
            return False

        self._direction = self.calculate_direction(self._pos)
        self._pos = self.move(self._pos, self._direction, print_board)
        while self._pos is not None and not (0 in self._pos or NUM_COL - 1 == self._pos[1] or NUM_ROWS - 1 == self._pos[0]):
            self._pos = self.move(self._pos, self._direction, print_board)

        return self._pos

    def move(self, pos, direction, print_board):
        row, col = pos

        r_shift, c_shift = MOVE_DICT[direction]
        next_pos = (row + r_shift, col + c_shift)
        if self._board.is_atom(next_pos):
            if print_board:
                print_board[row][col] = RAY_CHARS[direction][direction]
            return None

        next_dir = self._board.calculate_deflection(pos, direction)
        if next_dir != direction:
            if 0 in pos or NUM_COL - 1 == pos[1] or NUM_ROWS - 1 == pos[0]:
                return pos
            else:
                next_dir = self._board.calculate_deflection(pos, next_dir)

        if print_board:
            print_board[row][col] = RAY_CHARS[direction][next_dir]

        r_shift, c_shift = MOVE_DICT[next_dir]
        pos = (row + r_shift, col + c_shift)
        self._direction = next_dir

        return pos

    def calculate_direction(self, pos: tuple) -> str:
        row, col = pos

        if row == 0:
            return DOWN

        if row == 9:
            return UP

        if col == 0:
            return RIGHT

        return LEFT
