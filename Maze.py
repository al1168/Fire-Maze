import sys
import pygame
import math
from queue import PriorityQueue
import random
import Node
from algo import BFS, DFS, astar
from copy import copy, deepcopy
import algo

pygame.display.set_caption("CS440 Proj1")

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption(" Path Finding Algorithm")


def printgrid(grid, rows):
    for i in range(rows):
        for j in range(rows):
            cell = grid[i][j]
            print('[' + str(cell.row) + ']' + ' [' + str(cell.col) + ']' + ' ' + str(cell.color))
            # print(str(cell.color))


def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, Node.GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, Node.GREY, (j * gap, 0), (j * gap, width))


def draw(win, grid, rows, width):
    win.fill(Node.OPEN)

    for row in grid:
        for cell in row:
            cell.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()


def create_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            cell = Node.Cell(i, j, gap, rows)
            grid[i].append(cell)

    return grid


def copy_grid(grid):
    num_row = len(grid)
    grid_copy = []
    for i in range(num_row):
        grid_copy.append([])
        for j in range(num_row):
            curr = grid[i][j]
            cell = Node.Cell(i, j, curr.width, curr.total_rows)
            cell.color = curr.color
            cell.x = curr.x
            cell.y = curr.y
            cell.is_start = curr.is_start
            cell.is_target = curr.is_target
            cell.is_blocked = curr.is_blocked
            cell.is_closed = curr.is_closed
            cell.is_on_fire = curr.is_on_fire
            grid_copy[i].append(cell)
    for row in grid:
        for cell in row:
            cell.update_neighbors(grid_copy)
    return grid_copy


def advance_fire_one_step(grid, q):
    grid_copy = copy_grid(grid)

    for row in grid:
        for cell in row:
            k = 0
            if cell.color == Node.WHITE:
                for neighbor in cell.neighbors:
                    # print(neighbor.color)
                    if neighbor.is_on_fire():
                        k += 1
            probability = 1 - ((1 - q) ** k)
            random_num = random.uniform(0, 1)
            print(k)
            print(probability)
            print(random_num)
            if random_num <= probability:
                grid[cell.row][cell.col].set_on_fire()
                print('[' + str(cell.row) + ']' + ' [' + str(cell.col) + ']')

    return grid_copy


def generate_maze(grid, dim, p, density):
    start = grid[0][0].set_start()
    origin = grid[0][0]
    end = grid[dim - 1][dim - 1]
    target = grid[dim - 1][dim - 1].set_target()

    blockedCount = 0

    cnt = 0
    while density > 0:
        x = random.randrange(dim)
        y = random.randrange(dim)
        cell = grid[x][y]
        if cnt == (dim * dim) - 2:  # if the entire maze is blocked
            break
        if cell.is_start() or cell.is_target() or cell.is_blocked():
            continue
        cell.set_blocked()
        blockedCount += 1
        # print(cell.color)
        density -= 1
        cnt += 1
        # print("#" + str(cnt) + ": (" + str(x) + "," + str(y) + ")")
    print(str(blockedCount) + " blocked cells")


def reset(grid):
    for row in grid:
        for cell in row:
            if cell.is_start() or cell.is_target() or cell.is_blocked():
                continue
            cell.state = Node.OPEN


def main(win, width, dimension, prob):
    dim = dimension
    p = prob
    density = (dim ** 2) * p
    grid = create_grid(dim, width)

    generate_maze(grid, dim, p, density)
    print("Maze is generated")
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
                if event.key == pygame.K_SPACE and grid[0][0]:
                    for row in grid:
                        for cell in row:
                            cell.state = Node.OPEN
                    generate_maze(grid, dim, p, density)
                    print("Maze is generated\n \n ")

                # BFS
                if event.key == ord('b') and grid[0][0]:
                    reset(grid)
                    for row in grid:
                        for cell in row:
                            cell.update_neighbors(grid)
                    ret = BFS(lambda: draw(win, grid, dim, width), grid, grid[0][0], dim)
                    if ret == True:
                        print("BFS completed")
                    else:
                        print("BFS Path does not exist")
                # DFS
                if event.key == ord('d') and grid[0][0]:
                    reset(grid)
                    for row in grid:
                        for cell in row:
                            cell.update_neighbors(grid)
                    # astar

                    ret = DFS(lambda: draw(win, grid, dim, width), grid, grid[0][0], dim)
                    if ret == True:
                        print("DFS completed")
                    else:
                        print("DFS Path does not exist")
                if event.key == ord('a') and grid[0][0]:
                    reset(grid)
                    for row in grid:
                        for cell in row:
                            cell.update_neighbors(grid)
                    ret = astar(lambda: draw(win, grid, dim, width), grid, grid[0][0], dim, grid[dim - 1][dim - 1])
                    if ret == True:
                        print("Astar completed")
                    else:
                        print("Astar Path does not exist")
                if event.key == ord('f') and grid[0][0]:
                    for row in grid:
                        for cell in row:
                            cell.update_neighbors(grid)
                        rand_row = random.randrange(dim)
                        rand_col = random.randrange(dim)
                    if not grid[rand_row][rand_col].is_blocked() and not grid[rand_row][rand_col].is_on_fire():
                        grid[rand_row][rand_col].set_on_fire()
                    b = advance_fire_one_step(grid, 0.12)
                if event.key == pygame.K_RETURN:
                    reset(grid)
                    print("Maze Reset")

    pygame.quit()



if __name__ == '__main__':
    dimension = int(sys.argv[1])
    prob = float(sys.argv[2])
    main(WIN, WIDTH, dimension, prob)
    print("\nData:")
    print(algo.DATA)
