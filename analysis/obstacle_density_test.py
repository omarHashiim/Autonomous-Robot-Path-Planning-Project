import random

from core.grid import Grid
from analysis.performance_comparison import PerformanceComparison


ROWS = 20
COLS = 30

# Obstacle density levels
DENSITY_LEVELS = {
    "Low": 0.10,
    "Medium": 0.25,
    "High": 0.40
}


def generate_grid(density, seed=42):

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


def run_density_tests():

    comparison = PerformanceComparison(repetitions=10)

    all_results = {}

    for level, density in DENSITY_LEVELS.items():

        print(f"\nTesting {level} Obstacle Density ({density * 100:.0f}%)")

        grid = generate_grid(density)

        results = comparison.compare(grid)

        comparison.display_results(results)

        all_results[level] = results

    return all_results


if __name__ == "__main__":

    run_density_tests()