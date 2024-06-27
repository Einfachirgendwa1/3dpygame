# pyright:strict
import pygame

pygame.init()

SCREEN = (1000, 800)
FPS = 60

screen = pygame.display.set_mode(SCREEN)
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((50, 50, 50))
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
