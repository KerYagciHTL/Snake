import pygame
from src.utils.config import WIDTH, HEIGHT, TITLE, FONT_SIZE
from src.utils.color import BLACK, WHITE
from src.entities.grid import Grid
from src.entities.player import Player


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

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_w:
                    self.player.set_direction(0, -1)
                elif event.key == pygame.K_s:
                    self.player.set_direction(0, 1)
                elif event.key == pygame.K_a:
                    self.player.set_direction(-1, 0)
                elif event.key == pygame.K_d:
                    self.player.set_direction(1, 0)

    def update(self, dt):
        self.player.update(dt)
        if not self.player.alive:
            self.game_over = True

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
        pygame.display.flip()

    def run(self):
        while self.running:
            dt = self.clock.tick(60)
            self.handle_events()
            self.update(dt)
            self.draw()

        pygame.quit()
