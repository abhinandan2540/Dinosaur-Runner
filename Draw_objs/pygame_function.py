
# making a diagram consisting of rectangle and circle

import pygame


def drawingFunction(x, y, width, height):

    circle_x = width/2+x
    circle_y = height/2+y

    if (height < width):
        circle_r = height/2
    else:
        circle_r = width/2

    pygame.draw.rect(screen, "blue", [x, y, width, height])
    pygame.draw.circle(screen, "green", [circle_x, circle_y], circle_r)


pygame.init()
screen = pygame.display.set_mode((600, 600), pygame.RESIZABLE)
screen.fill("white")
drawingFunction(50, 200, 500, 200)
pygame.display.update()

keepRunning = True
while keepRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepRunning = False

pygame.quit()
