from queue import PriorityQueue
import math
import Node

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

#return a list of path nodes
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
        #node.set_color()
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
