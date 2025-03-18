from collections import deque

def bfs_shortest_path(graph, start, goal):
    queue = deque([(start, [start])])  # Queue holds tuples of (current_node, path)
    visited = set()

    while queue:
        current_node, path = queue.popleft()
        if current_node == goal:
            return path
        if current_node not in visited:
            visited.add(current_node)
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    return None  # Return None if no path is found

# Example city map
city_map = {
    'Home': ['Mall', 'School'],
    'Mall': ['Gym', 'Hospital'],
    'School': ['Library'],
    'Gym': ['Hospital'],
    'Library': ['Hospital'],
    'Hospital': []
}

# Running the BFS
start = 'Home'
goal = 'Hospital'
shortest_path = bfs_shortest_path(city_map, start, goal)

if shortest_path:
    print(f"Jalur terpendek dari {start} ke {goal}: {' -> '.join(shortest_path)}")
else:
    print(f"Tidak ada jalur yang ditemukan dari {start} ke {goal}")
