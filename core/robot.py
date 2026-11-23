class Robot:

    def __init__(self, start_position):

        # Robot's current position
        self.position = start_position

        # Store the movement history
        self.visited_positions = [start_position]

    # Move robot to a new position
    def move_to(self, new_position):

        self.position = new_position

        self.visited_positions.append(new_position)

    # Reset robot position
    def reset(self, start_position):

        self.position = start_position

        self.visited_positions = [start_position]