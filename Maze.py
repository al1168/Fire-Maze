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


def DFS(draw, grid, start):
    fringe = [start]
    while fringe:
        '#explore fringe'
        current = fringe.pop()
        for cell in current.neighbors:
            print(str(cell.color))
            print(str(cell.row) + ' ' + str(cell.col))
    return True


def main(win, width, dimension, prob):
    dim = dimension
    p = prob
    density = (dim ** 2) * p

    grid = create_grid(dim, width)

    start = grid[0][0].set_start()
    origin = grid[0][0]
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
    printgrid(grid, dim)
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
                    DFS(lambda: draw(win, grid, dim, width), grid, origin)
    pygame.quit()


if __name__ == '__main__':
    dimension = int(sys.argv[1])
    prob = float(sys.argv[2])
    main(WIN, WIDTH, dimension, prob)
