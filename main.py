# python
import pygame

MAX_CELL_SIZE = 32
WIDTH, HEIGHT = 800, 600
TITLE = "Snake"

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
font = pygame.font.Font(None, 48)

show_text = False
text_surface = font.render("Hello, World!", True, (255, 255, 255))

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_SPACE:
                show_text = not show_text

    if MAX_CELL_SIZE > 0:
        for x in range(0, WIDTH, MAX_CELL_SIZE):
            pygame.draw.line(screen, (60, 60, 60), (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, MAX_CELL_SIZE):
            pygame.draw.line(screen, (60, 60, 60), (0, y), (WIDTH, y))

    if show_text:
        screen.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2,
                                   HEIGHT // 2 - text_surface.get_height() // 2))

    pygame.display.flip()

pygame.quit()
