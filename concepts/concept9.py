
# pygame.time.get_ticks
# it will store the time in ticks variable

import pygame
import sys
pygame.init()

screen = pygame.display.set_mode((400, 500), pygame.RESIZABLE)

color = "red"

# taking time before running the loop
last_time = pygame.time.get_ticks()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

#    taking time during the time of loop
    current_time = pygame.time.get_ticks()

    if current_time-last_time >= 1000:
        if (color == "red"):
            color = "green"
        else:
            color = "red"
        last_time = current_time

    screen.fill(color)
    pygame.display.flip()
