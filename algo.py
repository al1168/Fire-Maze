from queue import PriorityQueue
import math
import Node
import random
from collections.abc import Iterable

DATA = []


class Data:
    def __init__(self):
        self.path = 0
        self.explored = 0
        self.graph_type = ""


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


# return a list of path nodes
def reconstruct_path(came_from, current, draw):
    path = []
    cnt = 0
    while current in came_from:
        cnt += 1
        current = came_from[current]
        # print("printing:" + '[' + str(current.row) + ']' + ' [' + str(current.col) + ']')
        current.set_path()
        path.append(current.get_pos())
        draw()
        # print(cnt)
    print(path)
    return path


def DFS(draw, grid, start, dim):
    my_data = Data()
    visited = set()
    # stack = [start]
    stack = StackFringe()
    stack.push(start)
    came_from = {}
    while not stack.is_empty():
        node = stack.pop()
        # node.set_color()
        # print("exploring:" + '[' + str(node.row) + ']' + ' [' + str(node.col) + ']')
        if node.row == dim - 1 and node.col == dim - 1:
            # print(len(came_from))
            path = reconstruct_path(came_from, node, draw)
            my_data.graph_type = "DFS"
            my_data.path = len(path)
            my_data.explored = len(visited)
            DATA.append([my_data.graph_type, my_data.path, my_data.explored])

            print(str(len(path)) + " in path")
            print(str(len(visited)) + " explored")
            return True

        if node not in visited:
            visited.add(node)
            node.set_explored()

        for neighbor in node.neighbors:
            if neighbor not in visited:
                stack.push(neighbor)
                came_from[neighbor] = node
    draw()
    print(str(len(visited) - 1) + " explored")

    my_data.graph_type = "DFS"
    my_data.path = 0 - 1
    my_data.explored = len(visited) - 1
    DATA.append([my_data.graph_type, my_data.path, my_data.explored])

    return False


def BFS(draw, grid, start, dim):
    my_data = Data()
    queue = Queue()
    visited = set()
    queue.enqueue(start)
    visited.add(start)

    came_from = {}
    cnt = 0
    while queue.size() > 0:
        curr = queue.dequeue()
        cnt += 1
        # print(cnt)
        # print('[' + str(curr.row) + ']' + ' [' + str(curr.col) + ']' + ' ' + str(curr.color))
        if curr.row == dim - 1 and curr.col == dim - 1:
            path = reconstruct_path(came_from, curr, draw)

            my_data.graph_type = "BFS"
            my_data.path = len(path)
            my_data.explored = len(visited)
            DATA.append([my_data.graph_type, my_data.path, my_data.explored])

            print(str(len(path)) + " in path")
            print(str(len(visited)) + " explored")
            return True

        for neighbor in curr.neighbors:
            if neighbor not in visited:
                neighbor.set_explored()
                visited.add(neighbor)
                queue.enqueue(neighbor)
                came_from[neighbor] = curr

    draw()
    print(str(len(visited) - 1) + " explored")

    my_data.graph_type = "BFS"
    my_data.path = 0
    my_data.explored = len(visited) - 1
    DATA.append([my_data.graph_type, my_data.path, my_data.explored])

    return False


def heuristic(start, end):
    euclidean_distance = math.sqrt((start.row - end.row) ** 2 + (start.col - end.col) ** 2)
    return euclidean_distance


def astar(draw, grid, start, dim, target):
    my_data = Data()
    came_from = {}
    closed_list = []
    open_list = PriorityQueue()
    open_list.put((0, start))
    g_score = {Node: float("inf") for row in grid for Node in row}
    g_score[start] = 0
    f_score = {Node: float("inf") for row in grid for Node in row}
    f_score[start] = heuristic(start, target)
    while not open_list.empty():
        curr = open_list.get()[1]
        curr.set_explored()
        if curr == target:
            path = reconstruct_path(came_from, curr, draw)
            my_data.graph_type = "Astar"
            my_data.path = len(path)
            my_data.explored = len(closed_list)
            DATA.append([my_data.graph_type, my_data.path, my_data.explored])

            print(str(len(path)) + " in path")
            print(str(len(closed_list)) + " explored")
            return True

        for neighbor in curr.neighbors:
            temp_g_score = g_score[curr] + 1
            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = curr
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + heuristic(neighbor, target)
                if neighbor not in closed_list:
                    open_list.put((f_score[neighbor], neighbor))
                    closed_list.append(neighbor)
        draw()
        if curr != start:
            curr.set_closed()

    print(str(len(closed_list)) + " explored")

    my_data.graph_type = "Astar"
    my_data.path = 0
    my_data.explored = len(closed_list)
    DATA.append([my_data.graph_type, my_data.path, my_data.explored])

    return False


def agent_astar(start, grid, target, strat):
    came_from = {}
    closed_list = []
    open_list = PriorityQueue()
    open_list.put((0, start))
    g_score = {Node: float("inf") for row in grid for Node in row}
    g_score[start] = 0
    f_score = {Node: float("inf") for row in grid for Node in row}
    f_score[start] = heuristic(start, target)
    while not open_list.empty():
        curr = open_list.get()[1]
        # print('[' + str(curr.row) + ']' + ' [' + str(curr.col) + ']' + ' ' + str(curr.state))
        # curr.set_explored()
        if curr == target:
            path = agent_path(came_from, curr)
            if strat == 1:
                return path
            if strat == 2:
                step = []
                # print(path)
                if(len(path)>=2):
                    step.append(path[-2])
                else:
                    step.append((len(grid)-1,len(grid)-1))
                return step
        for neighbor in curr.neighbors:
            # print('THIS IS current ['+str(curr.row) + ']' + ' [' + str(curr.col) + ']' + ' ' + str(curr.state))
            # print('THIS IS THE NEIGHBOR[' + str(neighbor.row) + ']' + ' [' + str(neighbor.col) + ']' + ' ' + str(neighbor.state))
            # print('THIS  THE  GSCORE'+str(g_score[neighbor]))
            temp_g_score = g_score[curr] + 1
            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = curr
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + heuristic(neighbor, target)
                if neighbor not in closed_list:
                    open_list.put((f_score[neighbor], neighbor))
                    closed_list.append(neighbor)
        if curr != start:
            curr.set_closed()


def agent_path(came_from, current):
    path = []
    cnt = 0
    while current in came_from:
        cnt += 1
        current = came_from[current]
        path.append(current.get_pos())
    # print(path)
    return path


def StrategyOne(agent, grid, target, draw, q):
    agent_pos = grid[int(agent.row)][int(agent.col)]
    path = []
    astar_list = agent_astar(agent_pos, grid, target, 1)
    if not isinstance(astar_list, Iterable):
        print("error occurred try again")
        return
    path.extend(astar_list)
    agent_pos.set_as_agent()
    draw()
    path_so_far = {}
    if len(path) <= 0:
        print("Agent insta died")
        return
    if len(path) > 0:
        path.pop()
    while len(path) > 0:
        next_step = path.pop()
        # print("next step = " + str(next_step))
        agent.row = next_step[0]
        agent.col = next_step[1]
        agent.set_pos(grid[int(agent.row)][int(agent.col)])
        agent_pos = agent.get_pos()
        if agent_pos.is_on_fire():
            print("Agent died")
            return
        agent_pos.set_as_agent()
        advance_fire_one_step(grid,q)
        draw()
    print("GOAL REACHED!")


# redefine  the fire as a block and compute shortest path given just that.
# move
# rinse repeat

def StrategyTwo(agent, grid, target, draw, q):
    agent_pos = grid[int(agent.row)][int(agent.col)]
    path = []
    came_from ={}
    dim = len(grid)
    # printgrid(alter,len(alter))
    # print("\n\n\n\n\n\n\n")
    # printgrid(grid,len(grid))
    cnt = 0
    while not agent.get_pos() == target:
        alter = alterMaze(grid)
        # print(cnt)
        # printgrid(alter, len(alter))
        # print("\n\n\n\n")
        # printgrid(grid,len(grid))
        agent_copy = Node.Agent(alter[int(agent.row)][int(agent.col)], int(agent.row), int(agent.col))
        agent_copy_pos = agent_copy.get_pos()
        target_copy = alter[dim - 1][dim - 1]
        # print('Agent_copy is:[ ' +str(int(agent_copy.row))+ '] '+ ' ['+str(int(agent_copy.col)) + '] ')
        # print(cnt)
        astar_move = agent_astar(agent_copy_pos, alter, target_copy, 2)
        if not isinstance(astar_move, Iterable):
            print("no path found")
            break
        if len(astar_move) < 1:
            print("no path is possible")
            break
        move = astar_move.pop()
        agent_row = move[0]
        agent_col = move[1]
        curr = grid[agent.row][agent.col]
        agent.set_pos(grid[agent_row][agent_col])
        agent.row = agent_row
        agent.col = agent_col
        came_from[grid[agent.row][agent.col]] = curr
        if agent.get_pos().is_on_fire():
            print("agent died")
            return
        if agent.get_pos() == target:
            print("goal reached!")
            agent.get_pos().set_as_agent()
            reconstruct_path(came_from,curr,draw)
            break
        agent.get_pos().set_as_agent()
        advance_fire_one_step(grid, q)
        draw()
        cnt += 1
    print("END?")


def advance_fire_one_step(grid, q):
    grid_copy = copy_grid(grid, 0)
    for row in grid:
        for cell in row:
            k = 0
            if cell.state == Node.OPEN or cell.state == Node.AGENT:
                for neighbor in cell.neighbors:
                    # print(neighbor.color)
                    if neighbor.is_on_fire():
                        k += 1
            else:
                continue
            probability = 1 - ((1 - q) ** k)
            random_num = random.uniform(0, 1)
            if random_num <= probability:
                grid[cell.row][cell.col].set_on_fire()
                # print('SETTING [' + str(cell.row) + ']' + ' [' + str(cell.col) + ']')
    return grid_copy


def alterMaze(grid):
    grid_copy = copy_grid(grid, 1)
    for row in grid_copy:
        for cell in row:
            if cell.is_on_fire():
                cell.set_blocked()
    for row in grid_copy:
        for cell in row:
            cell.update_neighbors(grid_copy)
    # printgrid(grid, len(grid))
    # print("\n\n\whatn\n\n\n")
    # printgrid(grid_copy,len(grid_copy))
    # print("\nend")
    return grid_copy

    # mode = 0 if need to update neighbors now
    # mode = 1 if need to update  neighbors later


def copy_grid(grid, mode):
    num_row = len(grid)
    grid_copy = []
    for i in range(num_row):
        grid_copy.append([])
        for j in range(num_row):
            curr = grid[i][j]
            cell = Node.Cell(i, j, curr.width, curr.total_rows)
            cell.row = curr.row
            cell.col = curr.col
            cell.x = curr.x
            cell.y = curr.y
            cell.state = curr.state
            cell.is_closed = curr.is_closed
            cell.width = curr.width
            cell.total_rows = curr.total_rows
            grid_copy[i].append(cell)
    if mode == 0:
        for row in grid_copy:
            for cell in row:
                cell.update_neighbors(grid_copy)
    return grid_copy


# def create_grid(rows, width):
#     grid = []
#     gap = width // rows
#     for i in range(rows):
#         grid.append([])
#         for j in range(rows):
#             cell = Node.Cell(i, j, gap, rows)
#             grid[i].append(cell)
#
#     return grid
def printgrid(grid, rows):
    for i in range(rows):
        for j in range(rows):
            cell = grid[i][j]
            print('[' + str(cell.row) + ']' + ' [' + str(cell.col) + ']' + ' ' + str(cell.state) + ' ' + str(
                cell.neighbors))
            # print(str(cell.color))
