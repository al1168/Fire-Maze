from queue import PriorityQueue
import math

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


def reconstruct_path(came_from, current, draw):
    cnt = 0
    while current in came_from:
        cnt += 1
        current = came_from[current]
        print("printing:" + '[' + str(current.row) + ']' + ' [' + str(current.col) + ']')
        current.set_path()
        draw()
        print(cnt)


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


def astar(draw, grid, start, dim, end):
    came_from = {}
    closed_list = []
    open_list = PriorityQueue()
    open_list.put((0, start))
    g_score = {Node: float("inf") for row in grid for Node in row}
    g_score[start] = 0
    f_score = {Node: float("inf") for row in grid for Node in row}
    f_score[start] = heuristic(start, end)
    while not open_list.empty():
        curr = open_list.get()[1]
        if curr == end:
            reconstruct_path(came_from, curr, draw)
            return True

        for neighbor in curr.neighbors:
            temp_g_score = g_score[curr] + 1
            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = curr
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + heuristic(neighbor, end)
                if neighbor not in closed_list:
                    open_list.put((f_score[neighbor], neighbor))
                    closed_list.append(neighbor)
                    neighbor.set_color()
        draw()
        if curr != start:
            curr.set_closed()
