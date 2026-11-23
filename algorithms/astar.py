import time
import heapq


def heuristic(position, goal):
    """
    Manhattan Distance Heuristic
    """
    row1, col1 = position
    row2, col2 = goal

    return abs(row1 - row2) + abs(col1 - col2)


def astar(grid):

    start_time = time.perf_counter()

    start = grid.start
    goal = grid.goal

    # Priority Queue: (f_score, g_score, position)
    priority_queue = [
        (heuristic(start, goal), 0, start)
    ]

    # Cost from start
    g_score = {start: 0}

    # Store previous cells
    parent = {start: None}

    explored_nodes = 0

    while priority_queue:

        f_cost, current_cost, current = heapq.heappop(priority_queue)

        # Ignore outdated entries
        if current_cost > g_score.get(current, float("inf")):
            continue

        explored_nodes += 1

        if current == goal:
            break

        for neighbor in grid.get_neighbors(current):

            new_cost = current_cost + 1

            if new_cost < g_score.get(neighbor, float("inf")):

                g_score[neighbor] = new_cost

                parent[neighbor] = current

                new_f_cost = new_cost + heuristic(neighbor, goal)

                heapq.heappush(
                    priority_queue,
                    (new_f_cost, new_cost, neighbor)
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