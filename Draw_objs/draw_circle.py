

import pygame
import sys

screen = pygame.display.set_mode((400, 500), pygame.RESIZABLE)
screen.fill("white")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

# drawing a circle
    pygame.draw.circle(screen, (0, 0, 255), [100, 200], 50, 2)
    pygame.display.update()
