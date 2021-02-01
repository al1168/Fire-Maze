import pygame

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
		self.color = GREEN

	def set_closed(self):
		self.is_closed = True
	def set_blocked(self):
		self.color = BLACK

	def set_target(self):
		self.is_target = True
		self.color = BLUE

	def set_path(self):
		self.color = GREY
	def set_on_fire():
		self.color = RED

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





