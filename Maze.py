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


# def DFS(draw, grid, start, dim):
#     visited = set()
#     camefrom = {}
#
#     path = DFSuntil(draw, grid, start, visited, dim, camefrom)
#     return path

#
# def reconstruct_path(came_from, current, draw):
#     cnt = 0
#     while current in came_from:
#         cnt += 1
#         current = came_from[current]
#         print("printing:" + '[' + str(current.row) + ']' + ' [' + str(current.col) + ']')
#         current.set_path()
#         draw()
#         print(cnt)


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

# def DFS(draw, grid, start, dim):
#     visited = set()
#     # stack = [start]
#     stack = StackFringe()
#     stack.push(start)
#     came_from = {}
#     while not stack.is_empty():
#         node = stack.pop()
#         print("exploring:" + '[' + str(node.row) + ']' + ' [' + str(node.col) + ']')
#         if node.row == dim - 1 and node.col == dim - 1:
#             # print(len(came_from))
#             reconstruct_path(came_from, node, draw)
#             break
#
#         if node not in visited:
#             visited.add(node)
#             node.set_current()
#             draw()
#
#         for neighbor in node.neighbors:
#             if neighbor not in visited:
#                 neighbor.set_color()
#                 draw()
#                 stack.push(neighbor)
#                 came_from[neighbor] = node
#
#     return True
#
#
# def BFS(draw, grid, start, dim):
#     queue = Queue()
#     visited = set()
#     queue.enqueue(start)
#     visited.add(start)
#
#     came_from = {}
#     cnt = 0
#     while queue.size() > 0:
#         curr = queue.dequeue()
#         curr.set_current()
#         cnt += 1
#         print(cnt)
#         print('[' + str(curr.row) + ']' + ' [' + str(curr.col) + ']' + ' ' + str(curr.color))
#         if curr.row == dim - 1 and curr.col == dim - 1:
#             reconstruct_path(came_from, curr, draw)
#             break
#         for neighbor in curr.neighbors:
#             if neighbor not in visited:
#                 neighbor.set_color()
#                 draw()
#                 visited.add(neighbor)
#                 queue.enqueue(neighbor)
#                 came_from[neighbor] = curr
#     return True
#
#
# def heuristic(start, end):
#     euclidean_distance = math.sqrt((start.row - end.row) ** 2 + (start.col - end.col) ** 2)
#     return euclidean_distance
#
#
# def astar(draw, grid, start, dim, end):
#     came_from = {}
#     closed_list = []
#     open_list = PriorityQueue()
#     open_list.put((0, start))
#     g_score = {Node: float("inf") for row in grid for Node in row}
#     g_score[start] = 0
#     f_score = {Node: float("inf") for row in grid for Node in row}
#     f_score[start] = heuristic(start, end)
#     while not open_list.empty():
#         curr = open_list.get()[1]
#         if curr == end:
#             reconstruct_path(came_from, curr, draw)
#             return True
#
#         for neighbor in curr.neighbors:
#             temp_g_score = g_score[curr] + 1
#             if temp_g_score < g_score[neighbor]:
#                 came_from[neighbor] = curr
#                 g_score[neighbor] = temp_g_score
#                 f_score[neighbor] = temp_g_score + heuristic(neighbor, end)
#                 if neighbor not in closed_list:
#                     open_list.put((f_score[neighbor], neighbor))
#                     closed_list.append(neighbor)
#                     neighbor.set_color()
#         draw()
#         if curr!= start:
#             curr.set_closed()

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
                    print("Maze is generated")

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
                    print("Maze Reset")

    pygame.quit()


if __name__ == '__main__':
    dimension = int(sys.argv[1])
    prob = float(sys.argv[2])
    main(WIN, WIDTH, dimension, prob)
