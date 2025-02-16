# MAKING PYGAME WINDOW RESIZABLE
import pygame
pygame.init()

screen = pygame.display.set_mode((400, 500), pygame.RESIZABLE)

# set_caption() : helps to write the heading of the pygame window
pygame.display.set_caption("PyGame Resizable Window")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
