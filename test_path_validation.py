from core.grid import Grid
from algorithms.bfs import bfs
from algorithms.dfs import dfs
from algorithms.dijkstra import dijkstra
from algorithms.astar import astar


algorithms = {
    "BFS": bfs,
    "DFS": dfs,
    "Dijkstra": dijkstra,
    "A*": astar
}


for name, algorithm in algorithms.items():

    grid = Grid(10, 10)

    grid.add_obstacle((2, 3))
    grid.add_obstacle((2, 4))
    grid.add_obstacle((3, 3))

    result = algorithm(grid)
    path = result["path"]

    print(f"\n========== {name} PATH VALIDATION ==========")

    checks = {
        "Starts at Start": bool(path) and path[0] == grid.start,
        "Ends at Goal": bool(path) and path[-1] == grid.goal,
        "Avoids Obstacles": bool(path) and all(
            position not in grid.obstacles for position in path
        ),
        "Valid Moves": bool(path) and all(
            abs(path[i][0] - path[i - 1][0]) +
            abs(path[i][1] - path[i - 1][1]) == 1
            for i in range(1, len(path))
        ),
        "Correct Path Length": result["path_length"] == len(path) - 1
    }

    for check_name, passed in checks.items():
        print(f"{check_name}: {'PASS' if passed else 'FAIL'}")

    print("Path Length:", result["path_length"])

    if all(checks.values()):
        print(f"{name}: ALL VALIDATION TESTS PASSED")
    else:
        print(f"{name}: VALIDATION FAILED")