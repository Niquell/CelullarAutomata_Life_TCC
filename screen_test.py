from screen import Screen
import numpy as np
import time

side = 100
data = np.random.rand(side, side) * 30
colors = ['white', 'red', 'green']
bounds = [0, 10, 20, 30]

s = Screen(data, colors, bounds)
s.show()
time.sleep(1)

s.frame(np.random.rand(side, side) * 30)
time.sleep(1)
s.frame(np.random.rand(side, side) * 30)
time.sleep(1)
s.frame(np.random.rand(side, side) * 30)
time.sleep(1)
s.frame(np.random.rand(side, side) * 30)
time.sleep(1)
s.frame(np.random.rand(side, side) * 30)
time.sleep(1)
