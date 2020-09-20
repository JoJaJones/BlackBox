from constants import *
from BlackBoxGame import BlackBoxGame

game = BlackBoxGame([(3, 2), (4, 2), (3, 7), (3, 4), (6, 4), (8, 7)])
run = True
while run:
    row = input("Row: ")
    col = input("Col: ")

    try:
        row = int(row)
        col = int(col)
        run = 0 <= row <= NUM_ROWS - 1
        run = run and 0 <= col <= NUM_COL - 1
    except:
        run = False

    if run:
        if 0 < row < NUM_ROWS -1 and 0 < col < NUM_COL - 1:
            game.guess_atom(row, col)
        else:
            game.shoot_ray(row, col)
        print(f"Atoms left: {game.atoms_left()}")
        print(f"Score: {game.get_score()}")