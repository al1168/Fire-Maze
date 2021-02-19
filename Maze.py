import sys
import pygame
import math
from queue import PriorityQueue
import random
import Node
import algo
from algo import BFS, DFS, astar
from copy import copy, deepcopy
import model

pygame.display.set_caption("CS440 Proj1")

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption(" Path Finding Algorithm")



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

def apply_model(grid, dim):
    #print("applying model")

    for i in range(0, dim):
        for j in range(0, dim):
            grid[i][j].set_danger_value(model.MODEL[i][j])

            #print("Danger Value:  "+str(grid[i][j].get_danger_value()))

def main(win, width, dimension, prob):
    dim = dimension
    p = prob
    density = (dim ** 2) * p
    grid = create_grid(dim, width)

    generate_maze(grid, dim, p, density)
    print("Maze is generated")

    m_rows, m_cols = (dim, dim)
    model = [[0 for i in range(m_cols)] for j in range(m_rows)]

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

                #A Star
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

                #Fire Maze
                if event.key == ord('f') and grid[0][0]:
                    for row in grid:
                        for cell in row:
                            cell.update_neighbors(grid)
                    count = 0
                    while count < 400:
                        count += 1
                        rand_row = random.randrange(dim)
                        rand_col = random.randrange(dim)
                        if not grid[rand_row][rand_col].is_blocked() and not grid[rand_row][rand_col].is_on_fire():
                            grid[rand_row][rand_col].set_on_fire()
                            break
                    # grid[4][6].set_on_fire()
                    # b = advance_fire_one_step(grid, 0.3)
                    agent = Node.Agent(grid[0][0], 0, 0)
                    # path = algo.StrategyOne(agent, grid, grid[dim - 1][dim - 1], lambda: draw(win, grid, dim, width), 0.5)
                    # path = algo.StrategyTwo(agent, grid, grid[dim - 1][dim - 1], lambda: draw(win, grid, dim, width), 0.3)
                    path = algo.StrategyThree(agent, grid, grid[dim - 1][dim - 1], lambda: draw(win, grid, dim, width), 0.3)
                    # apply_model(grid, dim)
                    # path = algo.StrategyThree(grid, grid[dim - 1][dim - 1], lambda: draw(win, grid, dim, width),
                    #                         0.3, dim)

                if event.key == ord('r') and grid[0][0]:
                    for row in grid:
                        for cell in row:
                            cell.update_neighbors(grid)
                    count = 0
                    while count < 400:
                        count += 1
                        rand_row = random.randrange(dim)
                        rand_col = random.randrange(dim)
                        if not grid[rand_row][rand_col].is_blocked() and not grid[rand_row][rand_col].is_on_fire():
                            grid[rand_row][rand_col].set_on_fire()
                            break
                    agent = Node.Agent(grid[0][0], 0, 0)
                    path = algo.StrategyTwo(agent, grid, grid[dim - 1][dim - 1],lambda: draw(win, grid, dim, width), 0.1)
                # Simulate Maze
                if event.key == ord('s') and grid[0][0]:
                    for row in grid:
                        for cell in row:
                            cell.update_neighbors(grid)

                            break
                    # b = advance_fire_one_step(grid, 0.3)

                    count = 0
                    while count < 400:
                        count += 1
                        rand_row = random.randrange(dim)
                        rand_col = random.randrange(dim)
                        if not grid[rand_row][rand_col].is_blocked() and not grid[rand_row][rand_col].is_on_fire():
                            grid[rand_row][rand_col].set_on_fire()
                            break
                    agent = Node.Agent(grid[0][0], 0, 0)
                    algo.StrategyThree(agent, grid, grid[dim-1][dim-1], lambda: draw(win, grid, dim, width), 0.3)



                    # m = algo.Strat3Simulation(grid, 1, dim)
                    # for i in range(0, dim):
                    #     for j in range(0, dim):
                    #         model[i][j] = model[i][j] + m[i][j]


                #reset Maze
                if event.key == pygame.K_RETURN:
                    reset(grid)
                    print("Maze Reset")





    pygame.quit()



def generate_data(win, width, dimension, prob):
    dim = dimension
    p = prob
    density = (dim ** 2) * p
    grid = create_grid(dim, width)

    generate_maze(grid, dim, p, density)

    print("Generating data starting...")

    # draw(win, grid, dim, width)
    for i in range(0, 10):
        BFS(lambda: draw(win, grid, dim, width), grid, grid[0][0], dim)
        generate_maze(grid, dim, p, density)
        print(str(i) + "trial done")
    # pygame.quit(
    print("Generation complete")


if __name__ == '__main__':
    dimension = int(sys.argv[1])
    prob = float(sys.argv[2])
    main(WIN, WIDTH, dimension, prob)
    print("\nData:")
    print(algo.DATA)
    #print(model.MODEL)
    '''
    print("print model5")
    for i in range(0, 5):
        for j in range(0, 5):
            print(model.MODEL5[i][j])
    '''