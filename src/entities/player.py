import pygame
from src.utils.config import WIDTH, HEIGHT, MAX_CELL_SIZE
from src.utils.color import GREEN


class Player:
    def __init__(self, grid_x, grid_y):
        self.max_grid_x = WIDTH // MAX_CELL_SIZE
        self.max_grid_y = HEIGHT // MAX_CELL_SIZE

        self.grid_x = grid_x
        self.grid_y = grid_y
        self.body = []
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
        if (self.grid_x, self.grid_y) in self.body:
                self.alive = False

        self.move_timer += dt
        if self.move_timer >= self.move_delay:
            self.move_timer = 0
            self.grid_x += self.direction[0]
            self.grid_y += self.direction[1]

            if self.body:
                self.body.insert(0, (self.grid_x - self.direction[0], self.grid_y - self.direction[1]))
                self.body.pop()

            elif self.grid_x < 0 or self.grid_x > self.max_grid_x or \
                    self.grid_y < 0 or self.grid_y > self.max_grid_y:
                self.alive = False


    def add_body_segment(self):
        if self.body:
            tail_x, tail_y = self.body[-1]
            self.body.append((tail_x, tail_y))
        else:
            self.body.append((self.grid_x - self.direction[0], self.grid_y - self.direction[1]))

    def draw(self, screen):
        cell_size = MAX_CELL_SIZE
        pygame.draw.rect(
            screen,
            GREEN,
            (self.grid_x * cell_size, self.grid_y * cell_size, cell_size, cell_size)
        )
        for segment in self.body:
            pygame.draw.rect(
                screen,
                GREEN,
                (segment[0] * cell_size, segment[1] * cell_size, cell_size, cell_size)
            )


