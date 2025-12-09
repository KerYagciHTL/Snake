import pygame
from src.utils.config import MAX_CELL_SIZE
from src.utils.color import WHITE


class Grid:

    def __init__(self, width, height, cell_size=MAX_CELL_SIZE):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.color = WHITE

    def draw(self, screen):
        if self.cell_size > 0:
            for x in range(0, self.width, self.cell_size):
                pygame.draw.line(screen, self.color, (x, 0), (x, self.height))
            for y in range(0, self.height, self.cell_size):
                pygame.draw.line(screen, self.color, (0, y), (self.width, y))

