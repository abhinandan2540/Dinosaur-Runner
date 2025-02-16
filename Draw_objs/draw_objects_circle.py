import pygame
from pygame.locals import *


pygame.init()

screen = pygame.display.set_mode((600, 600), pygame.RESIZABLE)
screen.fill("white")

clicked_points = []

gameRun = True
while gameRun:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRun = False
        elif event.type == MOUSEBUTTONDOWN:
            position = event.pos
            clicked_points.append(position)

    for postion in clicked_points:
        pygame.draw.circle(screen, "red", position, 30)

    pygame.display.update()

pygame.quit()
