import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Hello World!")
font = pygame.font.Font(None, 74)

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
                show_text = show_text != True

    if show_text:
        screen.blit(text_surface, (250, 250))

    pygame.display.flip()

pygame.quit()