import pygame
from src.utils.config import MAX_CELL_SIZE
from src.utils.color import RED

class Food:

    def __init__(self, grid_x, grid_y):
        self.grid_x = grid_x
        self.grid_y = grid_y

    def draw (self, screen):
        cell_size = MAX_CELL_SIZE
        pygame.draw.rect(
            screen,
            RED,
            (self.grid_x * cell_size, self.grid_y * cell_size, cell_size, cell_size)
        )