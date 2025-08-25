from collections import deque
from map import Map
import heapq

def bfs(m: Map):
    """Breadth-first search on the map."""
    start = m.initial_state
    goals = set(m.goal_states)
    frontier = deque([start])
    explored = set()
    parent = {start: None}

    while frontier:
        state = frontier.popleft()
        if state in goals:
            return reconstruct_path(parent, state)

        explored.add(state)
        for neighbor in m.get_neighbors(state):
            if neighbor not in explored and neighbor not in frontier:
                parent[neighbor] = state
                frontier.append(neighbor)
    return None


def dfs(m: Map):
    """Depth-first search on the map."""
    start = m.initial_state
    goals = set(m.goal_states)
    frontier = [start]
    explored = set()
    parent = {start: None}

    while frontier:
        state = frontier.pop()
        if state in goals:
            return reconstruct_path(parent, state)

        explored.add(state)
        for neighbor in m.get_neighbors(state):
            if neighbor not in explored and neighbor not in frontier:
                parent[neighbor] = state
                frontier.append(neighbor)
    return None

def manhattan_distance(a, b):
    """Heuristic function: Manhattan distance"""
    (x1, y1), (x2, y2) = a, b
    return abs(x1 - x2) + abs(y1 - y2)

def greedy_best_first_search(m):
    """Greedy Best-First Search"""
    start = m.initial_state
    goals = m.goal_states
    frontier = []
    heapq.heappush(frontier, (0, start))
    came_from = {start: None}
    visited = set()

    while frontier:
        _, current = heapq.heappop(frontier)

        if current in goals:
            # reconstruct path
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        if current in visited:
            continue
        visited.add(current)

        for neighbor in m.get_neighbors(current):
            if neighbor not in visited:
                priority = min(manhattan_distance(neighbor, g) for g in goals)
                if neighbor not in came_from:
                    came_from[neighbor] = current
                heapq.heappush(frontier, (priority, neighbor))

    return None  # No path found

def a_star_search(m):
    """A* Search"""
    start = m.initial_state
    goals = m.goal_states
    frontier = []
    heapq.heappush(frontier, (0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}

    while frontier:
        _, current = heapq.heappop(frontier)

        if current in goals:
            # reconstruct path
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        for neighbor in m.get_neighbors(current):
            new_cost = cost_so_far[current] + 1  # assume uniform cost grid
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + min(manhattan_distance(neighbor, g) for g in goals)
                heapq.heappush(frontier, (priority, neighbor))
                came_from[neighbor] = current

    return None


def reconstruct_path(parent, goal):
    """Reconstruct path from start to goal using parent links."""
    path = []
    state = goal
    while state is not None:
        path.append(state)
        state = parent[state]
    path.reverse()
    return path
