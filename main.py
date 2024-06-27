# pyright:strict
import pygame

pygame.init()

SCREEN = (1000, 800)

pygame.display.set_mode(SCREEN)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
