
# SAMPLE SURFACES
import pygame
pygame.init()

screen = pygame.display.set_mode((400, 500), pygame.RESIZABLE)
pygame.display.set_caption("Rectangle")
keepRunning = True


while keepRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepRunning = False

    pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(60, 100, 100, 60))
    pygame.display.update()

pygame.quit()
