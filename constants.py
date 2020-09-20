NUM_ROWS = 10
NUM_COL = NUM_ROWS

UP = "up"
RIGHT = "right"
DOWN = "down"
LEFT = "left"

DIRECTIONS = [UP, RIGHT, DOWN, LEFT]
DEFLECTORS = {UP: [(-1, -1), (-1, 1)], RIGHT: [(-1, 1), (1, 1)], DOWN: [(1, 1), (1, -1)], LEFT: [(1, -1), (-1, -1)]}
DEFLECT_DIRECTION = {0: 1, 1: -1}

MOVE_DICT = {LEFT: (0, -1), RIGHT: (0, 1), UP: (-1, 0), DOWN: (1, 0)}

RAY_CHARS = {
    RIGHT: {UP: "═╝ ", RIGHT: "═══", DOWN: "═╗ ", LEFT: "═══"},
    LEFT:  {UP: " ╚═", RIGHT: "═══", DOWN: " ╔═", LEFT: "═══"},
    UP:    {UP: " ║ ", RIGHT: " ╔═", DOWN: " ║ ", LEFT: "═╗ "},
    DOWN:  {UP: " ║ ", RIGHT: " ╚═", DOWN: " ║ ", LEFT: "═╝ "}
}

ATOM = " A "

START_SCORE = 25
SCORE_PER_USED = 1
SCORE_PER_GUESS = 5

DEBUG = True

CLEAR_COLOR = "\033[0m"
CONTENT_COLOR = "\033[36;107m"
USED_COLOR = "\033[30;46m"
GUESSED_COLOR = "\033[30;41m"
BORDER_COLOR = "\033[97;40m"
ATOM_COLOR = "\033[93;107m"
ATOM_GUESS = "\033[30;44m"
