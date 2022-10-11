import random
from screen import Screen
import numpy as np
import time

CA = __import__('2B')
side = 40


def life(cells):
    total = 0
    for cell in cells:
        if cell == 0:
            total += 1
    return total


def fire(cells):
    total = 0
    for cell in cells:
        if cell == 1:
            total += 1
    return total


def ashes(cells):
    total = 0
    for cell in cells:
        if cell == 2:
            total += 1
    return total


def fogo(curr, neigh):
    if curr == 0 and fire(neigh) > 3:
        return 1

    if curr == 1 and fire(neigh) > 7:
        return 2

    if curr == 1 and fire(neigh) < ashes(neigh):
        return 2

    return curr


arr = []
choices = [0, 0, 0, 0, 0, 0, 0, 1]
for i in range(side):
    arr.append([])
    for j in range(side):
        arr[i].append(random.choice(choices))

colors = ['white', 'red', 'black']
bounds = [0, 1, 2, 3]

_2B = CA.CellularAutomata(arr, fogo)

s = Screen(_2B.cells, colors, bounds)

while True:
    s.frame(_2B.cells)
    _2B.evolve()
    time.sleep(0.1)
