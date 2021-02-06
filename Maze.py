import sys
import pygame
import math
from queue import PriorityQueue
import random
import Node

pygame.display.set_caption("CS440 Proj1")

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Path Finding Algorithm")


class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)


class StackFringe:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def pop(self):
        return self.stack.pop()

    def push(self, loc):
        if loc in self.stack:
            return
        else:
            return self.stack.append(loc)

def create_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            cell = Node.Cell(i, j, gap, rows)
            grid[i].append(cell)

    return grid


def printgrid(grid, rows):
    for i in range(rows):
        for j in range(rows):
            cell = grid[i][j]
            print('[' + str(cell.row) + ']' + ' [' + str(cell.col) + ']' + ' ' + str(cell.color))


def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, Node.GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, Node.GREY, (j * gap, 0), (j * gap, width))


def draw(win, grid, rows, width):
    win.fill(Node.WHITE)

    for row in grid:
        for cell in row:
            cell.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()


# def DFS(draw, grid, start, dim):
#     visited = set()
#     camefrom = {}
#
#     path = DFSuntil(draw, grid, start, visited, dim, camefrom)
#     return path


def reconstruct_path(came_from, current, draw):
    cnt = 0
    while current in came_from:
        cnt += 1
        current = came_from[current]
        print("printing:" + '[' + str(current.row) + ']' + ' [' + str(current.col) + ']')
        current.set_path()
        draw()
        print(cnt)

# def DFSuntil(draw, grid, node, visited, dim, camefrom):
#     if node.row == dim - 1 and node.col == dim - 1:
#         reconstruct_path(camefrom, node, draw)
#         return True
#
#     visited.add(node)
#     for neighbor in node.neighbors:
#         if neighbor not in visited:
#             camefrom[neighbor] = node
#             neighbor.set_color()
#             draw()
#             DFSuntil(draw, grid, neighbor, visited, dim, camefrom)

def DFS(draw, grid, start, dim):
    visited = set()
    # stack = [start]
    stack = StackFringe()
    stack.push(start)
    came_from = {}
    while not stack.is_empty():
        node = stack.pop()
        print("exploring:" + '[' + str(node.row) + ']' + ' [' + str(node.col) + ']')
        if node.row == dim - 1 and node.col == dim - 1:
            # print(len(came_from))
            reconstruct_path(came_from, node, draw)
            break

        if node not in visited:
            visited.add(node)
            node.set_current()
            draw()

        for neighbor in node.neighbors:
            if neighbor not in visited:
                neighbor.set_color()
                draw()
                stack.push(neighbor)
                came_from[neighbor] = node

    return True

def BFS(draw, grid, start, dim):
    queue = Queue()
    visited = set()
    queue.enqueue(start)
    visited.add(start)

    came_from = {}
    cnt = 0
    while queue.size() > 0:
        curr = queue.dequeue()
        curr.set_current()
        cnt += 1
        print(cnt)
        print('[' + str(curr.row) + ']' + ' [' + str(curr.col) + ']' + ' ' + str(curr.color))
        if curr.row == dim - 1 and curr.col == dim - 1:
            reconstruct_path(came_from, curr, draw)
            break
        for neighbor in curr.neighbors:
            if neighbor not in visited:
                neighbor.set_color()
                draw()
                visited.add(neighbor)
                queue.enqueue(neighbor)
                came_from[neighbor] = curr
    return True


def heuristic(start, end):
    euclidean_distance = math.sqrt((start.row - end.row) ** 2 + (start.col - end.col) ** 2)
    return euclidean_distance


def astar(draw, grid, start, dim):
    came_from = {}



def main(win, width, dimension, prob):
    dim = dimension
    p = prob
    density = (dim ** 2) * p
    grid = create_grid(dim, width)

    start = grid[0][0].set_start()
    origin = grid[0][0]
    end = grid[dim - 1][dim - 1]
    target = grid[dim - 1][dim - 1].set_target()

    cnt = 0
    while density > 0:
        x = random.randrange(dim)
        y = random.randrange(dim)
        cell = grid[x][y]
        if cnt == (dim * dim) - 2:  # if the entire maze is blocked
            break
        if cell.is_start or cell.is_target or cell.is_blocked():
            continue
        cell.set_blocked()
        print(cell.color)
        density -= 1
        cnt += 1
        print("#" + str(cnt) + ": (" + str(x) + "," + str(y) + ")")

    print("Maze Created Now Generating...")
    '''
    #testign neighbors
    testCell = grid[1][2]
    testCell.update_neighbors(grid)
    nei = testCell.get_neighbors()
    print(len(nei))
    for i in nei:
        print(i.get_pos())
    '''
    run = True
    while run:
        draw(win, grid, dim, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and origin:
                    for row in grid:
                        for cell in row:
                            cell.update_neighbors(grid)
                    #DFS(lambda: draw(win, grid, dim, width), grid, origin, dim)
                    BFS(lambda: draw(win, grid, dim, width), grid, origin, dim)

    pygame.quit()


if __name__ == '__main__':
    dimension = int(sys.argv[1])
    prob = float(sys.argv[2])
    main(WIN, WIDTH, dimension, prob)
