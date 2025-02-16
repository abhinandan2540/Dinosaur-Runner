import pygame
pygame.init()

screen = pygame.display.set_mode((400, 500), pygame.RESIZABLE)

color = (255, 255, 0)
screen.fill(color)
pygame.display.flip()


keepRuning = True

while keepRuning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepRuning = False

# for making a circle in the pyGame screen
    pygame.draw.circle(screen, "black", (230, 250), 80)
    pygame.display.update()


pygame.quit()
