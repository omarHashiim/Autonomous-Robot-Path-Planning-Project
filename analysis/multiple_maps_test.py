import random
import csv
from statistics import mean

from core.grid import Grid
from algorithms.algorithm_manager import AlgorithmManager


ROWS = 20
COLS = 30

MAPS_PER_DENSITY = 100

DENSITY_LEVELS = {
    "10%": 0.10,
    "20%": 0.20,
    "25%": 0.25,
    "30%": 0.30,
    "35%": 0.35,
    "40%": 0.40
}


def generate_grid(density, seed):

    random.seed(seed)

    grid = Grid(ROWS, COLS)

    total_cells = ROWS * COLS
    obstacle_count = int(total_cells * density)

    available_positions = [
        (row, col)
        for row in range(ROWS)
        for col in range(COLS)
        if (row, col) not in (grid.start, grid.goal)
    ]

    obstacles = random.sample(
        available_positions,
        obstacle_count
    )

    for obstacle in obstacles:
        grid.add_obstacle(obstacle)

    return grid


def run_experiment():

    manager = AlgorithmManager()

    all_results = {}

    for level, density in DENSITY_LEVELS.items():

        print(f"\n========== {level} OBSTACLE DENSITY ==========")

        level_results = {
            name: {
                "times": [],
                "paths": [],
                "explored": [],
                "success": 0
            }
            for name in manager.get_algorithm_names()
        }

        for map_number in range(MAPS_PER_DENSITY):

            grid = generate_grid(
                density,
                seed=1000 + map_number
            )

            for algorithm_name in manager.get_algorithm_names():

                result = manager.run_algorithm(
                    algorithm_name,
                    grid
                )

                data = level_results[algorithm_name]

                data["times"].append(
                    result["execution_time"]
                )

                data["explored"].append(
                    result["explored_nodes"]
                )

                if result["path"]:

                    data["success"] += 1

                    data["paths"].append(
                        result["path_length"]
                    )

        all_results[level] = level_results

        print(f"\nMaps Tested: {MAPS_PER_DENSITY}")

        print(
            f"{'Algorithm':<12}"
            f"{'Avg Time':<16}"
            f"{'Avg Path':<14}"
            f"{'Avg Explored':<16}"
            f"{'Success %':<12}"
        )

        print("-" * 70)

        for name, data in level_results.items():

            avg_time = mean(data["times"])
            avg_explored = mean(data["explored"])

            avg_path = (
                mean(data["paths"])
                if data["paths"]
                else 0
            )

            success_rate = (
                data["success"] / MAPS_PER_DENSITY
            ) * 100

            print(
                f"{name:<12}"
                f"{avg_time:<16.8f}"
                f"{avg_path:<14.2f}"
                f"{avg_explored:<16.2f}"
                f"{success_rate:<12.1f}"
            )

    # Save results to CSV

    with open(
        "analysis/results.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "Density",
            "Algorithm",
            "Average Time",
            "Average Path Length",
            "Average Explored Nodes",
            "Success Rate"
        ])

        for level, algorithms in all_results.items():

            for name, data in algorithms.items():

                writer.writerow([
                    level,
                    name,
                    mean(data["times"]),
                    mean(data["paths"]) if data["paths"] else 0,
                    mean(data["explored"]),
                    (data["success"] / MAPS_PER_DENSITY) * 100
                ])

    print("\n========================================")
    print("EXPERIMENT COMPLETED")
    print("Results saved to: analysis/results.csv")
    print("========================================")

    return all_results


if __name__ == "__main__":

    run_experiment()