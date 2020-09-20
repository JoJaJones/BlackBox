from Board import Board
from Ray import Ray
from Display import Display
from constants import *

class BlackBoxGame:
    def __init__(self, atoms):
        self._board = Board(atoms)
        self._atoms = set(atoms)
        self._guesses = set()
        self._used = set()
        self._display = Display(atoms)

    def shoot_ray(self, row, col):
        curr_ray = Ray(self._board, (row, col))
        result = curr_ray.traverse(self._display.get_board())
        if result != False:
            self._used.add((row, col))

        if result is not None and result != False:
            self._used.add(result)

        if DEBUG:
            self._display.update_used(self._used)
            self._display.print_board()

        return result

    def guess_atom(self, row, col):
        self._guesses.add((row, col))

        if DEBUG:
            self._display.update_guessed(self._guesses)
            self._display.print_board()

        return self._board.is_atom((row, col))

    def atoms_left(self):
        return len(self._atoms.difference(self._guesses))

    def get_score(self):
        num_wrong_guesses = len(self._guesses.difference(self._atoms))
        used_edge_spaces = len(self._used)

        return START_SCORE - SCORE_PER_USED * used_edge_spaces - SCORE_PER_GUESS * num_wrong_guesses
