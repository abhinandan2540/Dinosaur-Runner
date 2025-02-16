
# pygame.draw.rect	Draws a rectangle on a Pygame surface.
# window	The surface(screen) where the rectangle is drawn.
# (0, 0, 255)	The color in RGB format(Blue in this case).
# [100, 100, 400, 100]	The rectangle position and size:
# 🔹 100, 100 →(X, Y) position(top-left corner).
# 🔹 400 → Width
# 🔹 100 → Height
# 0	Fill style:
# 🔹 0 → Solid filled rectangle
# 🔹 If > 0, it defines the border thickness.


import pygame
import sys


screen = pygame.display.set_mode((400, 500), pygame.RESIZABLE)
screen.fill("white")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.draw.rect(screen, (0, 0, 255), [100, 100, 200, 100], 2)
    pygame.display.update()
