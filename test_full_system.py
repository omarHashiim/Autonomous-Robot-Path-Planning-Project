from core.grid import Grid
from core.robot import Robot
from algorithms.algorithm_manager import AlgorithmManager


def validate_path(path, grid, result):

    if not path:
        return False

    # Check Start and Goal
    if path[0] != grid.start or path[-1] != grid.goal:
        return False

    # Check Obstacles
    if any(position in grid.obstacles for position in path):
        return False

    # Check Valid Movements
    for i in range(1, len(path)):
        distance = (
            abs(path[i][0] - path[i - 1][0]) +
            abs(path[i][1] - path[i - 1][1])
        )

        if distance != 1:
            return False

    # Check Path Length
    if result["path_length"] != len(path) - 1:
        return False

    return True


def run_full_system_test():

    print("\n========== FULL SYSTEM INTEGRATION TEST ==========")

    manager = AlgorithmManager()

    algorithms = manager.get_algorithm_names()

    print("\nAvailable Algorithms:", algorithms)

    for algorithm_name in algorithms:

        print(f"\n---------- {algorithm_name} ----------")

        # 1. Create Grid
        grid = Grid(10, 10)

        # 2. Add Obstacles
        grid.add_obstacle((2, 3))
        grid.add_obstacle((2, 4))
        grid.add_obstacle((3, 3))

        print("Grid Created: PASS")
        print("Obstacles Added: PASS")

        # 3. Run Algorithm
        result = manager.run_algorithm(algorithm_name, grid)

        path = result["path"]

        if not path:
            print("Path Generation: FAIL")
            continue

        print("Path Generation: PASS")

        # 4. Validate Path
        if validate_path(path, grid, result):
            print("Path Validation: PASS")
        else:
            print("Path Validation: FAIL")
            continue

        # 5. Create Robot and Execute Path
        robot = Robot(grid.start)

        for position in path[1:]:
            robot.move_to(position)

        if robot.position == grid.goal:
            print("Robot Reached Goal: PASS")
        else:
            print("Robot Reached Goal: FAIL")
            continue

        # 6. Check Movement History
        if robot.visited_positions == path:
            print("Movement History: PASS")
        else:
            print("Movement History: FAIL")
            continue

        # 7. Reset Robot
        robot.reset(grid.start)

        if robot.position == grid.start:
            print("Robot Reset: PASS")
        else:
            print("Robot Reset: FAIL")
            continue

        print("Path Length:", result["path_length"])
        print("Explored Nodes:", result["explored_nodes"])
        print("Execution Time:", result["execution_time"])

        print(f"{algorithm_name}: FULL TEST PASSED")

    print("\n========== FULL SYSTEM TEST COMPLETED ==========")


if __name__ == "__main__":
    run_full_system_test()