from constants import *

class Board:
    def __init__(self, atoms: list = None):
        self._positions = []
        for r in range(NUM_ROWS):
            self._positions.append([])
            for c in range(NUM_COL):
                self._positions[r].append("   ")

        if atoms is not None:
            for row, col in atoms:
                self._positions[row][col] = ATOM

    def add_atom(self, pos: tuple) -> None:
        row, col = pos
        self._positions[row][col] = ATOM

    def calculate_deflection(self, pos: tuple, direction: str):
        deflectors = DEFLECTORS[direction]
        row, col = pos
        for idx, pos in enumerate(deflectors):
            r_shift, c_shift = pos
            if self.is_atom((row + r_shift, col + c_shift)):
                dir_idx = DIRECTIONS.index(direction)
                dir_idx += DEFLECT_DIRECTION[idx] + 4
                dir_idx %= 4
                return DIRECTIONS[dir_idx]

        return direction

    def is_atom(self, pos: tuple) -> bool:
        row, col = pos
        if 0 <= row < NUM_ROWS and 0 <= col < NUM_COL:
            return self._positions[row][col] == ATOM
        else:
            return False
