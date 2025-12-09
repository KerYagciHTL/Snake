import pygame
from src.utils.config import MAX_CELL_SIZE
from src.utils.color import GREEN


class Player:

    def __init__(self, x, y, cell_size=MAX_CELL_SIZE):
        self.grid_x = x
        self.grid_y = y
        self.cell_size = cell_size
        self.color = GREEN

    @property
    def pixel_x(self):
        return self.grid_x * self.cell_size

    @property
    def pixel_y(self):
        return self.grid_y * self.cell_size

    def move(self, dx, dy, grid_width, grid_height):
        new_x = self.grid_x + dx
        new_y = self.grid_y + dy

        max_x = grid_width // self.cell_size
        max_y = grid_height // self.cell_size

        if 0 <= new_x < max_x and 0 <= new_y < max_y:
            self.grid_x = new_x
            self.grid_y = new_y

    def draw(self, screen):
        rect = pygame.Rect(self.pixel_x, self.pixel_y, self.cell_size, self.cell_size)
        pygame.draw.rect(screen, self.color, rect)

