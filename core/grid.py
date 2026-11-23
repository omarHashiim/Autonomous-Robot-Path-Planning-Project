class Grid:

    def __init__(self, rows=20, cols=30):

        self.rows = rows
        self.cols = cols

        # Robot starting position
        self.start = (0, 0)

        # Target position
        self.goal = (rows - 1, cols - 1)

        # Obstacles
        self.obstacles = set()

    # Check if a position is inside the grid
    def is_valid(self, position):

        row, col = position

        return (
            0 <= row < self.rows and
            0 <= col < self.cols
        )

    # Check if a cell is free
    def is_walkable(self, position):

        return (
            self.is_valid(position) and
            position not in self.obstacles
        )

    # Add obstacle
    def add_obstacle(self, position):

        if self.is_valid(position):

            if position != self.start and position != self.goal:
                self.obstacles.add(position)

    # Remove obstacle
    def remove_obstacle(self, position):

        self.obstacles.discard(position)

    # Get neighboring cells
    def get_neighbors(self, position):

        row, col = position

        directions = [
            (-1, 0),  # Up
            (1, 0),   # Down
            (0, -1),  # Left
            (0, 1)    # Right
        ]

        neighbors = []

        for dr, dc in directions:

            new_position = (row + dr, col + dc)

            if self.is_walkable(new_position):
                neighbors.append(new_position)

        return neighbors

    # Clear all obstacles
    def clear_obstacles(self):

        self.obstacles.clear()