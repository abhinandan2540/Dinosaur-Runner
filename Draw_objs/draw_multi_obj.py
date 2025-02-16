

import pygame
import sys

screen = pygame.display.set_mode((600, 600), pygame.RESIZABLE)
screen.fill("white")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.draw.rect(screen, "blue", [50, 200, 500, 200])
    pygame.draw.circle(screen, "green", [300, 300], 100)
    pygame.display.update()
