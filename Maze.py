import sys
import pygame
import math
from queue import PriorityQueue
import random
import Node
from algo import BFS, DFS, astar

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


def generate_maze(grid, dim, p, density):
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
        # print(cell.color)
        density -= 1
        cnt += 1
        # print("#" + str(cnt) + ": (" + str(x) + "," + str(y) + ")")


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
                            cell.color = Node.WHITE

                    generate_maze(grid, dim, p, density)
                    print("Maze is generated\n \n ")

                # BFS
                if event.key == ord('b') and grid[0][0]:
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
                    for row in grid:
                        for cell in row:
                            cell.update_neighbors(grid)
                    ret = DFS(lambda: draw(win, grid, dim, width), grid, grid[0][0], dim)
                    if ret == True:
                        print("DFS completed")
                    else:
                        print("DFS Path does not exist")
                if event.key == ord('a') and grid[0][0]:
                    for row in grid:
                        for cell in row:
                            cell.update_neighbors(grid)
                    ret = astar(lambda: draw(win, grid, dim, width), grid, grid[0][0], dim, grid[dim-1][dim-1])
                    if ret == True:
                        print("Astar completed")
                    else:
                        print("Astar Path does not exist")
                # Reset
                if event.key == pygame.K_RETURN:
                    for row in grid:
                        for cell in row:
                            if cell.is_start or cell.is_target or cell.is_blocked():
                                continue
                            # if cell.color == Node.TURQUOISE or cell.color == Node.PURPLE:
                            cell.color = Node.WHITE
                    print("Maze Reset \n")

    pygame.quit()


if __name__ == '__main__':
    dimension = int(sys.argv[1])
    prob = float(sys.argv[2])
    main(WIN, WIDTH, dimension, prob)
