import pygame
import math
from queue import PriorityQueue
import random
import Node
import globals

pygame.display.set_caption("CS440 Proj1")

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
		pygame.draw.line(win, globals.GREY, (0, i * gap), (width, i * gap))
		for j in range(rows):
			pygame.draw.line(win, globals.GREY, (j * gap, 0), (j * gap, width))


def draw(win, grid, rows, width):
	win.fill(globals.WHITE)

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
				density -= 1
				cell.set_blocked()

	run = True
	while run:
		draw(win, grid, dim, width)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

	pygame.quit()

if __name__ == '__main__':
	main(globals.WIN, globals.WIDTH)