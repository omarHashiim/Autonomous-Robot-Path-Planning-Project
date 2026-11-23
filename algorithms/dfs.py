import time


def dfs(grid):

    start_time = time.perf_counter()

    start = grid.start
    goal = grid.goal

    # Stack for DFS
    stack = [start]

    # Track visited cells
    visited = {start}

    # Store parent of each cell
    parent = {start: None}

    explored_nodes = 0

    while stack:

        current = stack.pop()

        explored_nodes += 1

        if current == goal:
            break

        for neighbor in grid.get_neighbors(current):

            if neighbor not in visited:

                visited.add(neighbor)

                parent[neighbor] = current

                stack.append(neighbor)

    # Reconstruct path
    path = []

    if goal in parent:

        current = goal

        while current is not None:

            path.append(current)

            current = parent[current]

        path.reverse()

    end_time = time.perf_counter()

    return {
        "path": path,
        "explored_nodes": explored_nodes,
        "execution_time": end_time - start_time,
        "path_length": len(path) - 1 if path else 0
    }