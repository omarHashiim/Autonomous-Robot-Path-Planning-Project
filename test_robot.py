from core.grid import Grid
from core.robot import Robot
from algorithms.astar import astar


# Create Grid
grid = Grid(10, 10)

grid.add_obstacle((2, 3))
grid.add_obstacle((2, 4))
grid.add_obstacle((3, 3))


# Generate Path using A*
result = astar(grid)
path = result["path"]


print("\n========== ROBOT MOVEMENT TEST ==========")

# Create Robot
robot = Robot(grid.start)

print("Initial Position:", robot.position)


# TEST 1: Path Availability
if path:
    print("TEST 1 PASSED: Path generated successfully.")
else:
    print("TEST 1 FAILED: No path available.")


# TEST 2: Execute Path
if path:
    for position in path[1:]:
        robot.move_to(position)

    print("Current Position:", robot.position)

    if robot.position == grid.goal:
        print("TEST 2 PASSED: Robot reached the Goal.")
    else:
        print("TEST 2 FAILED: Robot did not reach the Goal.")


# TEST 3: Movement History
if robot.visited_positions == path:
    print("TEST 3 PASSED: Movement history is correct.")
else:
    print("TEST 3 FAILED: Movement history mismatch.")


# TEST 4: Obstacle Avoidance
if all(position not in grid.obstacles for position in robot.visited_positions):
    print("TEST 4 PASSED: Robot avoided all obstacles.")
else:
    print("TEST 4 FAILED: Robot crossed an obstacle.")


# TEST 5: Reset
robot.reset(grid.start)

print("Position After Reset:", robot.position)

if robot.position == grid.start and robot.visited_positions == [grid.start]:
    print("TEST 5 PASSED: Robot reset successfully.")
else:
    print("TEST 5 FAILED: Robot reset error.")


print("=========================================")