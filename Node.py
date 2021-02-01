import globals
import pygame

class Cell:
	def __init__(self, row, col, width, total_rows):
		self.row = row
		self.col = col
		self.x = row * width
		self.y = col * width
		self.color = globals.WHITE
		self.is_start = False
		self.is_target = False
		self.is_closed = False
		self.is_on_fire = globals.RED
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
		return self.color == globals.BLACK
	def is_start(self):
		return self.is_start == True
	def is_target(self):
		return self.is_target == True
	def is_on_fire(self):
		return self.is_on_fire == globals.RED

	def set_start(self):
		self.is_start = True
		self.color = globals.GREEN

	def set_closed(self):
		self.is_closed = True
	def set_blocked(self):
		self.color = globals.BLACK

	def set_target(self):
		self.is_target = True
		self.color = globals.BLUE

	def set_path(self):
		self.color = globals.GREY
	def set_on_fire():
		self.color = globals.RED

	def draw(self, win):
		pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

	def update_neighbors(self, grid):
		self.neighbors = []
		if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_blocked(): # DOWN
			self.neighbors.append(grid[self.row + 1][self.col])

		if self.row > 0 and not grid[self.row - 1][self.col].is_blocked(): # UP
			self.neighbors.append(grid[self.row - 1][self.col])

		if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_blocked(): # RIGHT
			self.neighbors.append(grid[self.row][self.col + 1])

		if self.col > 0 and not grid[self.row][self.col - 1].is_blocked(): # LEFT
			self.neighbors.append(grid[self.row][self.col - 1])

	def __lt__(self, other):
		return False





