from core.grid import Grid

# Create grid
grid = Grid(10, 10)

# Add obstacles
grid.add_obstacle((2, 3))
grid.add_obstacle((2, 4))
grid.add_obstacle((3, 3))

# Display information
print("Grid Size:", grid.rows, "x", grid.cols)

print("Start:", grid.start)

print("Goal:", grid.goal)

print("Obstacles:", grid.obstacles)

print("Neighbors of (2, 2):", grid.get_neighbors((2, 2)))

print("Is (2, 3) walkable?", grid.is_walkable((2, 3)))

print("Is (2, 2) walkable?", grid.is_walkable((2, 2)))