
# we will see how to set up a game loop in PyGame. Game Loop is the loop that keeps the game running. It keeps running till the user wants to exit. While the game loop is running it mainly does the following tasks:

# Update our game window to show visual changes
# Update our game states based on user inputs
# Handle different types of events
# Keep game window running
# Simply game loop is a while loop having only one condition to check whether our boolean condition to keep the game running is true.


# GAME LOOP WITH CHANGING COLOR

import pygame
pygame.init()

screen = pygame.display.set_mode((400, 500), pygame.RESIZABLE)
color = "red"

keepGameRunning = True

while keepGameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGameRunning = False

    screen.fill(color)
    pygame.display.flip()

    if (color == "red"):
        color = "green"
    else:
        color = "red"

pygame.quit()
