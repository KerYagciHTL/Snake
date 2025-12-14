import pygame
from src.utils.config import WIDTH, HEIGHT, TITLE, FONT_SIZE
from src.utils.color import BLACK, WHITE
from src.entities.grid import Grid
from src.entities.player import Player
from src.entities.food import Food


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, FONT_SIZE)

        self.grid = Grid(WIDTH, HEIGHT)
        self.player = Player(5, 5)
        self.text_surface = self.font.render("Hello, World!", True, WHITE)
        self.running = True
        self.game_over = False
        self.food = Food()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    self.player.set_direction(0, -1)
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    self.player.set_direction(0, 1)
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    self.player.set_direction(-1, 0)
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.player.set_direction(1, 0)

    def update(self, dt):
        self.player.update(dt)
        self.game_over = not self.player.alive

        if self.player.grid_x == self.food.grid_x and self.player.grid_y == self.food.grid_y:
            self.player.add_body_segment()
            self.food.randomize_position()

    def draw(self):
        if self.game_over:
            self.screen.fill(BLACK)
            game_over_surface = self.font.render("Game Over!", True, WHITE)
            self.screen.blit(
                game_over_surface,
                ((WIDTH - game_over_surface.get_width()) // 2,
                 (HEIGHT - game_over_surface.get_height()) // 2)
            )
            pygame.display.flip()
            return

        self.screen.fill(BLACK)
        self.grid.draw(self.screen)
        self.player.draw(self.screen)
        self.food.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while self.running:
            dt = self.clock.tick(60)
            self.handle_events()
            self.update(dt)
            self.draw()

        pygame.quit()
