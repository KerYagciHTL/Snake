import pygame
from config import WIDTH, HEIGHT, TITLE, FONT_SIZE
from grid import Grid
from color import BLACK, WHITE


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, FONT_SIZE)

        self.grid = Grid(WIDTH, HEIGHT)
        self.show_text = False
        self.text_surface = self.font.render("Hello, World!", True, WHITE)
        self.running = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_SPACE:
                    self.show_text = not self.show_text

    def draw(self):
        self.screen.fill(BLACK)
        self.grid.draw(self.screen)

        if self.show_text:
            text_x = WIDTH // 2 - self.text_surface.get_width() // 2
            text_y = HEIGHT // 2 - self.text_surface.get_height() // 2
            self.screen.blit(self.text_surface, (text_x, text_y))

        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.draw()
            self.clock.tick(60)

        pygame.quit()
