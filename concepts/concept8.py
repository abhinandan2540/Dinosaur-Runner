import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400, 500), pygame.RESIZABLE)


# sec count on miliseconds
pygame.time.wait(2000)
color = "red"


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(color)
    pygame.display.flip()
