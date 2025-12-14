import pygame
import random
from src.utils.config import MAX_CELL_SIZE, WIDTH, HEIGHT
from src.utils.color import RED

class Food:

    def __init__(self, grid_x=None, grid_y=None):
        self.max_grid_x = WIDTH // MAX_CELL_SIZE
        self.max_grid_y = HEIGHT // MAX_CELL_SIZE

        if grid_x is None or grid_y is None:
            self.randomize_position()
        else:
            self.grid_x = grid_x
            self.grid_y = grid_y

    def randomize_position(self):
        self.grid_x = random.randint(0, self.max_grid_x - 1)
        self.grid_y = random.randint(0, self.max_grid_y - 1)

    def draw(self, screen):
        cell_size = MAX_CELL_SIZE
        pygame.draw.rect(
            screen,
            RED,
            (self.grid_x * cell_size, self.grid_y * cell_size, cell_size, cell_size)
        )