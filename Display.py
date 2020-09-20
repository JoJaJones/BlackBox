from constants import *


class Display:
    def __init__(self, atoms):
        self._display_board = []
        self._atoms = atoms
        self._used = set()
        self._guessed = set()
        self.reset_board()

    def reset_board(self):
        self._display_board = []
        for r in range(NUM_ROWS):
            self._display_board.append([])
            for c in range(NUM_COL):
                self._display_board[r].append("   ")

        for atom in self._atoms:
            r, c = atom
            self._display_board[r][c] = ATOM_COLOR + ATOM + CONTENT_COLOR

    def update_guessed(self, guessed):
        self._guessed = guessed

    def update_used(self, used):
        self._used = used

    def prep_board(self):
        for used in self._used:
            r, c = used
            self._display_board[r][c] = USED_COLOR + self._display_board[r][c] + CONTENT_COLOR

        for guessed in self._guessed:
            r, c = guessed
            if (r, c) in self._atoms:
                self._display_board[r][c] = ATOM_GUESS + ATOM + CONTENT_COLOR
            else:
                self._display_board[r][c] = GUESSED_COLOR + self._display_board[r][c] + CONTENT_COLOR

    def print_board(self):
        self.prep_board()
        print(BORDER_COLOR + " ╔═", end="")
        for col in range(NUM_COL):
            print("═══", end="")
            if col != NUM_COL - 1:
                print("═", end="")
        print("═╗ " + CLEAR_COLOR)

        for row in range(len(self._display_board)):
            print(BORDER_COLOR + " ║ " + CONTENT_COLOR, end="")
            print("|".join(self._display_board[row]), end="")
            print(BORDER_COLOR + " ║ " + CLEAR_COLOR)
            if row != NUM_ROWS - 1:
                print(BORDER_COLOR + " ║ " + CONTENT_COLOR, end="")
                for col in range(len(self._display_board[row])):
                    print("---", end="")
                    if col != NUM_COL - 1:
                        print("+", end="")
                print(BORDER_COLOR + " ║ " + CLEAR_COLOR)

        print(BORDER_COLOR + " ╚═", end="")
        for col in range(NUM_COL):
            print("═══", end="")
            if col != NUM_COL - 1:
                print("═", end="")
        print("═╝ " + CLEAR_COLOR)

        self.reset_board()

    def get_board(self):
        return self._display_board
