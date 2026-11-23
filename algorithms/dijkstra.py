import time
import heapq


def dijkstra(grid):

    start_time = time.perf_counter()

    start = grid.start
    goal = grid.goal

    # Priority Queue
    priority_queue = [(0, start)]

    # Store minimum costs
    distances = {start: 0}

    # Store previous cells
    parent = {start: None}

    explored_nodes = 0

    while priority_queue:

        current_cost, current = heapq.heappop(priority_queue)

        if current_cost > distances[current]:
            continue

        explored_nodes += 1

        if current == goal:
            break

        for neighbor in grid.get_neighbors(current):

            new_cost = current_cost + 1

            if new_cost < distances.get(neighbor, float("inf")):

                distances[neighbor] = new_cost

                parent[neighbor] = current

                heapq.heappush(
                    priority_queue,
                    (new_cost, neighbor)
                )

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