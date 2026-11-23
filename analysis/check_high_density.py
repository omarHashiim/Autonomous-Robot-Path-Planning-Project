from analysis.multiple_maps_test import generate_grid
from algorithms.algorithm_manager import AlgorithmManager

manager = AlgorithmManager()

total_maps = 100
successful_maps = 0
failed_maps = 0
total_explored = 0

print("========== 100 HIGH DENSITY MAPS ==========")

for map_number in range(total_maps):

    seed = 1000 + map_number

    grid = generate_grid(0.40, seed)

    result = manager.run_algorithm("BFS", grid)

    total_explored += result["explored_nodes"]

    if result["path"]:
        successful_maps += 1
    else:
        failed_maps += 1

success_rate = (successful_maps / total_maps) * 100
failure_rate = (failed_maps / total_maps) * 100
avg_explored = total_explored / total_maps

print("\n========== FINAL RESULTS ==========")
print("Total Maps:", total_maps)
print("Successful Maps:", successful_maps)
print("Failed Maps:", failed_maps)
print("Success Rate:", success_rate, "%")
print("Failure Rate:", failure_rate, "%")
print("Average Explored Nodes:", avg_explored)