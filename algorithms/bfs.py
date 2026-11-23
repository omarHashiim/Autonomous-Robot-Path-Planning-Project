from collections import deque
import time


def bfs(grid):

    start_time = time.perf_counter()

    start = grid.start
    goal = grid.goal

    # Queue for BFS
    queue = deque([start])

    # Track visited cells
    visited = {start}

    # Store the path
    parent = {start: None}

    explored_nodes = 0

    while queue:

        current = queue.popleft()
        explored_nodes += 1

        # Check if goal is reached
        if current == goal:
            break

        # Explore neighbors
        for neighbor in grid.get_neighbors(current):

            if neighbor not in visited:

                visited.add(neighbor)
                parent[neighbor] = current

                queue.append(neighbor)

    # Reconstruct path
    path = []

    if goal in parent:

        current = goal

        while current is not None:

            path.append(current)
            current = parent[current]

        path.reverse()

    end_time = time.perf_counter()

    execution_time = end_time - start_time

    return {
        "path": path,
        "explored_nodes": explored_nodes,
        "execution_time": execution_time,
        "path_length": len(path) - 1 if path else 0
    }