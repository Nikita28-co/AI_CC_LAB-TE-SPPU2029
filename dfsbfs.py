from collections import deque

# Create the graph as an adjacency list (dictionary of lists)
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5, 6],
    3: [1],
    4: [1],
    5: [2],
    6: [2]
}

# Recursive DFS
def dfs(graph, vertex, visited):
    visited.add(vertex)
    print(vertex, end=' ')
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Iterative BFS
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
# Perform DFS and BFS

print("Depth First Search (DFS):") 
dfs(graph, 0, set())

print("\nBreadth First Search (BFS):")
bfs(graph, 0)
