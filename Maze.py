import pygame
import math
from queue import PriorityQueue
import random
import Node

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Path Finding Algorithm")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)


def create_grid(rows, width):
	grid = []
	gap = width // rows
	for i in range(rows):
		grid.append([])
		for j in range(rows):
			cell = Node.Cell(i, j, gap, rows)
			grid[i].append(cell)

	return grid


def draw_grid(win, rows, width):
	gap = width // rows
	for i in range(rows):
		pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
		for j in range(rows):
			pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))


def draw(win, grid, rows, width):
	win.fill(WHITE)

	for row in grid:
		for cell in row:
			cell.draw(win)

	draw_grid(win, rows, width)
	pygame.display.update()



def main(win, width):
	dim = 10
	p = .1
	density = (dim ** 2) * p

	grid = create_grid(dim, width)

	start = grid[0][0].set_start()
	end = grid[dim-1][dim-1].set_target()


	for i in range(0, len(grid)):
		for cell in grid[i]:
			if density == 0:
				break
			elif(cell.is_start or cell.is_target):
				continue
			bool = random.getrandbits(1)
			if(bool == 1):
				density -= 0
				cell.set_blocked()

	run = True
	while run:
		draw(win, grid, dim, width)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

	pygame.quit()

main(WIN, WIDTH)