import numpy as np
import matplotlib.pyplot as plt
from math import fabs,sqrt

class Maze():
    def __init__(self, dim, prob):
        self.grid = np.random.choice(
                        a=[True, False],
                        size=(dim, dim),
                        p=[prob, 1-prob])
        self.grid[0][0] = False
        self.grid[dim-1][dim-1] = False 
        self.dim = dim
        self.prob = prob

    def render_maze(self):
        plt.imshow(self.grid, cmap='Greys',  interpolation='nearest')
        plt.show()


if __name__ == '__main__':
    dimension = int(input("What is the dim of the maze?\n"))
    percent = float(input("What is the p value a tile is blocked?\n"))
    mymaze = Maze(dimension, percent)
    mymaze.render_maze()