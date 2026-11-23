from core.grid import Grid
from algorithms.astar import astar


# ==============================
# TEST 1: Normal Path
# ==============================

grid = Grid(10, 10)

grid.add_obstacle((2, 3))
grid.add_obstacle((2, 4))
grid.add_obstacle((3, 3))

result = astar(grid)

print("\n========== A* NORMAL TEST ==========")
print("Path:", result["path"])
print("Path Length:", result["path_length"])
print("Explored Nodes:", result["explored_nodes"])
print("Execution Time:", result["execution_time"])


# ==============================
# TEST 2: No Path Available
# ==============================

grid = Grid(10, 10)

grid.add_obstacle((0, 1))
grid.add_obstacle((1, 0))

result = astar(grid)

print("\n========== A* NO PATH TEST ==========")
print("Path:", result["path"])
print("Path Length:", result["path_length"])
print("Explored Nodes:", result["explored_nodes"])

if result["path"] is None or len(result["path"]) == 0:
    print("TEST PASSED: No path detected correctly.")
else:
    print("TEST FAILED: Unexpected path found.")

print("====================================")