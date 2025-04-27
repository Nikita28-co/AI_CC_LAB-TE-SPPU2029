import heapq

def a_star(grid, start, goal):
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Manhattan distance

    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start, goal), 0, start))  # (f, g, node)
    came_from = {}
    g_score = {start: 0}

    while open_set:
        _, g, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                temp_g = g + 1
                if neighbor not in g_score or temp_g < g_score[neighbor]:
                    g_score[neighbor] = temp_g
                    f = temp_g + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f, temp_g, neighbor))
                    came_from[neighbor] = current

    return None  # No path found

# Test grid: 0 = walkable, 1 = wall
grid = [
    [0, 1, 0],
    [0, 1, 0],
    [0, 0, 0],
]

start = (0, 0)
goal = (2, 2)

path = a_star(grid, start, goal)
print("Path:", path)
