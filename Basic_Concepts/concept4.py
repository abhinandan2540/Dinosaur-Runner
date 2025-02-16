import pygame
pygame.init()

screen = pygame.display.set_mode((400, 500), pygame.RESIZABLE)
pygame.display.set_caption("Change BG")

# for setting background color
color = (255, 0, 0)
screen.fill(color)

# actually made the color of the BG
pygame.display.flip()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
