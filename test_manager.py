from core.grid import Grid
from algorithms.algorithm_manager import AlgorithmManager


grid = Grid(10, 10)

grid.add_obstacle((2, 3))
grid.add_obstacle((2, 4))
grid.add_obstacle((3, 3))

manager = AlgorithmManager()


# =================================
# TEST 1: Available Algorithms
# =================================

print("\n========== TEST 1: AVAILABLE ALGORITHMS ==========")

algorithms = manager.get_algorithm_names()

print("Available Algorithms:", algorithms)

if len(algorithms) == 4:
    print("TEST PASSED: All algorithms are available.")
else:
    print("TEST FAILED: Incorrect number of algorithms.")


# =================================
# TEST 2: Run All Algorithms
# =================================

print("\n========== TEST 2: RUN ALL ALGORITHMS ==========")

for algorithm_name in algorithms:

    result = manager.run_algorithm(algorithm_name, grid)

    print(f"\nAlgorithm: {algorithm_name}")
    print("Path Length:", result["path_length"])
    print("Explored Nodes:", result["explored_nodes"])
    print("Execution Time:", result["execution_time"])

    if result["path"]:
        print("TEST PASSED")
    else:
        print("TEST FAILED")


# =================================
# TEST 3: Invalid Algorithm Name
# =================================

print("\n========== TEST 3: INVALID ALGORITHM ==========")

try:
    manager.run_algorithm("INVALID", grid)
    print("TEST FAILED: Invalid algorithm was accepted.")

except ValueError as error:
    print("TEST PASSED: Invalid algorithm rejected.")
    print("Error:", error)


print("\n========== ALL TESTS COMPLETED ==========")