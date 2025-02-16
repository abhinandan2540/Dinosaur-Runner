import pygame
pygame.init()

screen = pygame.display.set_mode((400, 500))

# using get size we'll able to get the screen size of the screen of the pygame
x, y = screen.get_size()

# quitting the pygame engine
pygame.display.quit()

# printing the screen size
print(x, y)
