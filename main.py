import random
from screen import Screen
import numpy as np
import time

from cellularAutomata import CellularAutomata

side = 100

# arr = [
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 1, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0]
# ]

arr = []
choices = [0, 1]
for i in range(side):
    arr.append([])
    for j in range(side):
        arr[i].append(random.choice(choices))

colors = ['green', 'darkred']
bounds = [0, 1, 2]

_2B = CellularAutomata(arr)

s = Screen(_2B.cells, colors, bounds)
s.show()

while True:
    s.frame(_2B.cells)
    _2B.evolve()
    time.sleep(1)
