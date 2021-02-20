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

# basic Queue implementation
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

# basic Stack implementation
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
    # print(path)
    return path

# DFS Algorithm
# return boolean value if path is not found
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

# Breath First Search
# returns boolean value, True if path is found and false aif path is not found
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

# Heuristic function for computing A*
#  return integer
def heuristic(start, end):
    euclidean_distance = math.sqrt((start.row - end.row) ** 2 + (start.col - end.col) ** 2)
    return euclidean_distance

# A* implementation
# returns boolean True if path is found ,  false if path isn't found
def astar(draw, grid, start, dim, target):
    my_data = Data()
    came_from = {}
    closed_list = []
    open_list = PriorityQueue()
    open_list.put((0, start))
    # Using List comprehension, we set the g score and f score of all the nodes to inf initially
    g_score = {Node: float("inf") for row in grid for Node in row}
    g_score[start] = 0
    f_score = {Node: float("inf") for row in grid for Node in row}
    f_score[start] = heuristic(start, target)
    # loops the fringe
    while not open_list.empty():
        curr = open_list.get()[1]
        curr.set_explored()
        # if path found, reconstructs path by setting color on the pygame grid
        if curr == target:
            path = reconstruct_path(came_from, curr, draw)
            my_data.graph_type = "Astar"
            my_data.path = len(path)
            my_data.explored = len(closed_list)
            DATA.append([my_data.graph_type, my_data.path, my_data.explored])
            print(str(len(path)) + " in path")
            print(str(len(closed_list)) + " explored")
            return True
        # explore the neighbors and find an unexplored neighbor to explore based on the f score
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

# A* that returns a path or one step depending on the strategy
#
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
        if curr == target:
            path = agent_path(came_from, curr)
            if strat == 1:
                return path
            if strat == 2:
                step = []
                # print(path)
                if (len(path) >= 2):
                    step.append(path[-2])
                else:
                    step.append((len(grid) - 1, len(grid) - 1))
                return step
        for neighbor in curr.neighbors:
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

# returns a list of the path
def agent_path(came_from, current):
    path = []
    cnt = 0
    while current in came_from:
        cnt += 1
        current = came_from[current]
        path.append(current.get_pos())

    return path

# computes shortest path with A* algorithm
# follow the path and hope agent doesn't die
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
        advance_fire_one_step(grid, q)
        draw()
    print("GOAL REACHED!")


# redefine  the fire as a block and compute shortest path given just that.
# move a cell and advance fire
# recomputes the path  after each step
# repeat steps  2 and  3
def StrategyTwo(agent, grid, target, draw, q):
    agent_pos = grid[int(agent.row)][int(agent.col)]
    path = []
    came_from = {}
    dim = len(grid)
    cnt = 0
    while not agent.get_pos() == target:
        alter = alterMaze(grid)
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
            reconstruct_path(came_from, curr, draw)
            break
        agent.get_pos().set_as_agent()
        advance_fire_one_step(grid, q)
        draw()
        cnt += 1
    print("END?")

#takes the grid and increment a timestep for the fire
#  spreads based on the algorithm  below
def advance_fire_one_step(grid, q):
    # grid_copy = copy_grid(grid, 0)
    fire = []
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
                fire.append(grid[cell.row][cell.col])
                # print('SETTING [' + str(cell.row) + ']' + ' [' + str(cell.col) + ']')
    for cell in fire:
        cell.set_on_fire()
    return fire

# returns a maze that replaces the fire as a block
def alterMaze(grid):
    grid_copy = copy_grid(grid, 1)
    for row in grid_copy:
        for cell in row:
            if cell.is_on_fire():
                cell.set_blocked()
    for row in grid_copy:
        for cell in row:
            cell.update_neighbors(grid_copy)
    return grid_copy


# mode = 0 if need to update neighbors now
# mode = 1 if need to update  neighbors later
# interate the grid and return a copy of that grid
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
            cell.danger_value = curr.danger_value
            grid_copy[i].append(cell)
    if mode == 0:
        for row in grid_copy:
            for cell in row:
                cell.update_neighbors(grid_copy)
    return grid_copy

# print grid coordinates and its neighbors
def printgrid(grid, rows):
    for i in range(rows):
        for j in range(rows):
            cell = grid[i][j]
            print('[' + str(cell.row) + ']' + ' [' + str(cell.col) + ']' + ' ' + str(cell.state) + ' ' + str(
                cell.neighbors))
            # print(str(cell.color))

# simulates the fire to create  a danger value matrix
def fire_simulation(grid, q):
    num_row = len(grid)
    danger_matrix = []
    for i in range(num_row):
        danger_matrix.append([])
        for j in range(num_row):
            danger_matrix[i].append(0)
    rows = len(grid)
    sim_num = 0
    while sim_num < 60:
        grid_copy = copy_grid(grid, 0)
        for i in range(0, rows):
            fire = advance_fire_one_step(grid_copy, q)
        for row in grid_copy:
            for cell in row:
                if cell.is_on_fire():
                    danger_matrix[cell.row][cell.col] += 1
        sim_num += 1
    # print(danger_matrix)
    return danger_matrix

# 1.generate  a danger matrix
# 2.compute  a  path  with astar
# 3. follow the path, and hope agent  lives
def StrategyThree(agent, grid, target, draw, q):
    danger_matrix = fire_simulation(grid, q)
    came_from = {}
    for i in range(len(danger_matrix)):
        for j in range(len(danger_matrix)):
            grid[i][j].set_danger_value(danger_matrix[i][j])
    agent_pos = grid[int(agent.row)][int(agent.col)]
    path = []
    astar_list = asta(agent_pos, grid, target, 1,danger_matrix)
    if not isinstance(astar_list, Iterable):
        print("Cannot reach exit")
        return
    path.extend(astar_list)
    agent_pos.set_as_agent()
    draw()
    while True:
        if not isinstance(path, Iterable):
            print("no path found")
            break
        if len(path) < 1:
            print("GOAL")
            break
        # print("this is the path"+path)
        if agent.get_pos().is_on_fire():
            print("agent died")
            return
        step = path.pop()
        agent.row = step[0]
        agent.col = step[1]
        came_from[grid[agent.row][agent.col]] = agent.get_pos()
        agent.set_pos(grid[agent.row][agent.col])
        agent.get_pos().set_as_agent()
        if agent.get_pos().is_on_fire():
            print("agent died")
            return
        advance_fire_one_step(grid, q)
        draw()
        if(agent.get_pos==target):
            print('GOAL')
            break

# Astar with danger values added as a heuristic
def asta(start, grid, target, strat,danger_matrix):
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
        for neighbor in curr.neighbors:
            temp_g_score = g_score[curr] + 1
            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = curr
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + heuristic(neighbor, target)+danger_matrix[neighbor.row][neighbor.col]
                if neighbor not in closed_list:
                    open_list.put((f_score[neighbor], neighbor))
                    closed_list.append(neighbor)
        if curr != start:
            curr.set_closed()

