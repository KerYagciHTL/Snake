import pygame
from src.utils.config import WIDTH, HEIGHT, MAX_CELL_SIZE
from src.utils.color import GREEN


class Player:
    def __init__(self, grid_x, grid_y):
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.direction = (1, 0)
        self.move_timer = 0
        self.move_delay = 150
        self.alive = True

    def set_direction(self, dx, dy):
        if (dx, dy) != (-self.direction[0], -self.direction[1]):
            self.direction = (dx, dy)

    def update(self, dt):
        if not self.alive:
            return

        self.move_timer += dt
        if self.move_timer >= self.move_delay:
            self.move_timer = 0
            self.grid_x += self.direction[0]
            self.grid_y += self.direction[1]

            max_grid_x = WIDTH // MAX_CELL_SIZE
            max_grid_y = HEIGHT // MAX_CELL_SIZE

            if self.grid_x < 0 or self.grid_x > max_grid_x or \
                    self.grid_y < 0 or self.grid_y > max_grid_y:
                self.alive = False

    def draw(self, screen):
        cell_size = MAX_CELL_SIZE
        pygame.draw.rect(
            screen,
            GREEN,
            (self.grid_x * cell_size, self.grid_y * cell_size, cell_size, cell_size)
        )
