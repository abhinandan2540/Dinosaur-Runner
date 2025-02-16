# drawing a polygon

import pygame
import sys

screen = pygame.display.set_mode((400, 500), pygame.RESIZABLE)
screen.fill("white")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.draw.polygon(screen, (255, 0, 0),
                        [[300, 300], [100, 400],
                         [100, 300]])
    pygame.display.update()
