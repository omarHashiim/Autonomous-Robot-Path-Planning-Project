import pygame
import sys
import time

from core.grid import Grid
from core.robot import Robot
from algorithms.algorithm_manager import AlgorithmManager


pygame.init()

# Window settings
CELL_SIZE = 30
ROWS = 20
COLS = 30

WIDTH = COLS * CELL_SIZE
HEIGHT = ROWS * CELL_SIZE + 130

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Autonomous Robot Path Planning")

# Colors
WHITE = (255, 255, 255)
BLACK = (30, 30, 30)
GRAY = (200, 200, 200)
GREEN = (0, 200, 0)
RED = (220, 0, 0)
BLUE = (0, 100, 255)
YELLOW = (255, 220, 0)
PURPLE = (150, 0, 200)

font = pygame.font.SysFont("Arial", 20)

grid = Grid(ROWS, COLS)
manager = AlgorithmManager()

robot = Robot(grid.start)

selected_algorithm = "A*"
result = None

animation_path = []
robot_index = 0
animating = False
last_move_time = 0

MOVE_DELAY = 0.15


def draw_grid():

    screen.fill(WHITE)

    for row in range(ROWS):
        for col in range(COLS):

            position = (row, col)

            rect = pygame.Rect(
                col * CELL_SIZE,
                row * CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE
            )

            color = WHITE

            if position in grid.obstacles:
                color = BLACK

            elif result and position in result["path"]:
                color = YELLOW

            if position == grid.start:
                color = GREEN

            if position == grid.goal:
                color = RED

            if position == robot.position:
                color = PURPLE

            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, GRAY, rect, 1)

    info = font.render(
        f"Algorithm: {selected_algorithm} | 1:BFS 2:DFS 3:Dijkstra 4:A*",
        True,
        BLUE
    )
    screen.blit(info, (10, ROWS * CELL_SIZE + 10))

    instructions = font.render(
        "Left Click: Add Obstacle | Right Click: Remove",
        True,
        BLACK
    )
    screen.blit(instructions, (10, ROWS * CELL_SIZE + 40))

    run_text = font.render(
        "SPACE: Find Path | R: Reset | ENTER: Move Robot",
        True,
        BLUE
    )
    screen.blit(run_text, (10, ROWS * CELL_SIZE + 70))

    if result:
        stats = font.render(
            f"Path: {result['path_length']} | Explored: {result['explored_nodes']}",
            True,
            BLACK
        )
        screen.blit(stats, (10, ROWS * CELL_SIZE + 100))

    pygame.display.flip()


def reset_simulation():

    global result, animation_path, robot_index, animating

    grid.clear_obstacles()
    robot.reset(grid.start)

    result = None
    animation_path = []
    robot_index = 0
    animating = False


running = True
clock = pygame.time.Clock()

while running:

    current_time = time.time()

    # Robot Animation
    if animating and current_time - last_move_time >= MOVE_DELAY:

        if robot_index < len(animation_path):

            robot.move_to(animation_path[robot_index])
            robot_index += 1

        else:
            animating = False

        last_move_time = current_time

    draw_grid()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_1:
                selected_algorithm = "BFS"
                result = None

            elif event.key == pygame.K_2:
                selected_algorithm = "DFS"
                result = None

            elif event.key == pygame.K_3:
                selected_algorithm = "Dijkstra"
                result = None

            elif event.key == pygame.K_4:
                selected_algorithm = "A*"
                result = None

            elif event.key == pygame.K_SPACE:

                animating = False
                robot.reset(grid.start)

                result = manager.run_algorithm(
                    selected_algorithm,
                    grid
                )

                animation_path = result["path"][1:]
                robot_index = 0

            elif event.key == pygame.K_RETURN:

                if result and animation_path and not animating:
                    if robot.position != grid.goal:
                        animating = True
                        last_move_time = time.time()

            elif event.key == pygame.K_r:
                reset_simulation()

        elif event.type == pygame.MOUSEBUTTONDOWN:

            x, y = event.pos

            if y < ROWS * CELL_SIZE and not animating:

                col = x // CELL_SIZE
                row = y // CELL_SIZE

                position = (row, col)

                if event.button == 1:
                    grid.add_obstacle(position)

                elif event.button == 3:
                    grid.remove_obstacle(position)

                result = None
                robot.reset(grid.start)
                animation_path = []
                robot_index = 0


    clock.tick(60)


pygame.quit()
sys.exit()