import pygame
import math
from queue import PriorityQueue
import random

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

class Cell:
	def __init__(self, row, col, width, total_rows):
		self.row = row
		self.col = col
		self.x = row * width
		self.y = col * width
		self.color = WHITE
		self.is_start = False
		self.is_target = False
		self.is_closed = False
		self.is_on_fire = RED
		self.neighbors = []
		self.width = width
		self.total_rows = total_rows

	def get_pos(self):
		return self.row, self.col
	def get_color(self):
		return self.color

	def is_closed(self):
		return self.is_closed == True
	def is_blocked(self):
		return self.color == BLACK
	def is_start(self):
		return self.is_start == True
	def is_target(self):
		return self.is_target == True
	def is_on_fire(self):
		return self.is_on_fire == RED

	def set_start(self):
		self.is_start = True
		self.color = BLUE

	def set_closed(self):
		self.is_closed = True
	def set_blocked(self):
		self.color = BLACK

	def set_target(self):
		self.is_target = True
		self.color = TURQUOISE

	def set_path(self):
		self.color = GREEN
	def set_on_fire():
		self.color = RED

	def draw(self, win):
		pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

	def update_neighbors(self, grid):
		self.neighbors = []
		if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier(): # DOWN
			self.neighbors.append(grid[self.row + 1][self.col])

		if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): # UP
			self.neighbors.append(grid[self.row - 1][self.col])

		if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier(): # RIGHT
			self.neighbors.append(grid[self.row][self.col + 1])

		if self.col > 0 and not grid[self.row][self.col - 1].is_barrier(): # LEFT
			self.neighbors.append(grid[self.row][self.col - 1])

	def __lt__(self, other):
		return False


def create_grid(rows, width):
	grid = []
	gap = width // rows
	for i in range(rows):
		grid.append([])
		for j in range(rows):
			cell = Cell(i, j, gap, rows)
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