import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np


class Screen:
    def __init__(self, data, color_list, bounds):
        self.data = data
        self.cmap = colors.ListedColormap(color_list)
        self.bounds = bounds
        self.norm = colors.BoundaryNorm(bounds, self.cmap.N)
        self.fig, self.ax = plt.subplots()
        self.ax.grid(
            which='major',
            axis='both',
            linewidth=0.05
        )
        self.ax.set_xticks(np.arange(210, 200, 210))
        self.ax.set_yticks(np.arange(210, 200, 210))

    def show(self):
        self.fig, self.ax = plt.subplots()
        self.norm = colors.BoundaryNorm(self.bounds, self.cmap.N)
        self.ax.imshow(self.data, cmap=self.cmap, norm=self.norm)
        plt.show()

    def set_data(self, data):
        self.data = data

    def set_bounds(self, bounds):
        self.bounds = bounds
        self.norm = colors.BoundaryNorm(bounds, self.cmap.N)

    def set_colors(self, color_list):
        self.cmap = colors.ListedColormap(color_list)

    def frame(self, data):
        self.set_data(data)
        self.show()
