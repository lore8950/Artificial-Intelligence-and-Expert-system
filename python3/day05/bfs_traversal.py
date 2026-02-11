# BFS (Breadth First Search)

from collections import deque

def bfs(graph, start):
    visited = set([start])      # Mark the start node as visited
    queue = deque([start])      # Initialize queue with start node

    while queue:
        node = queue.popleft()  # Remove from front of queue
        print(node, end=' ')    # Print current node

        # Visit all neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Graph representation (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

# Run BFS starting from node 'A'
bfs(graph, 'A')
