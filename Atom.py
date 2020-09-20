# unneeded
from constants import *

for i in range(40, 56):
    if i > 47:
        i += 52
    for j in range(30, 46):
        if j > 37:
            j += 52
        print(f"\033[{j};{i}m {j:3}, {i:3}", end=" ")
        if j % 10 == 7:
            print(CLEAR_COLOR)