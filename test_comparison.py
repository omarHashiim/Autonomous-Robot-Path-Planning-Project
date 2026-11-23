from core.grid import Grid
from analysis.performance_comparison import PerformanceComparison


# Create test environment
grid = Grid(20, 30)

# Add obstacles
obstacles = [
    (5, 5), (5, 6), (5, 7),
    (6, 7), (7, 7),
    (10, 10), (10, 11), (10, 12),
    (11, 12), (12, 12),
    (15, 20), (15, 21), (15, 22)
]

for obstacle in obstacles:
    grid.add_obstacle(obstacle)


# Run performance comparison
comparison = PerformanceComparison(repetitions=10)

results = comparison.compare(grid)

comparison.display_results(results)