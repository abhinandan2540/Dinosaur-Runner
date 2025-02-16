
# First we import and initialize all imported modules.
# We use import pygame to import all modules and .init() function to initialize those modules.

import pygame
pygame.init()

# Initialize a window to display. We use .set_mode() function to create a window.
# We pass the width and height of our window as parameters to set_mode() function

width = 400
height = 500

pygame.display.set_mode((width, height))

# Keep that window running until the user presses the exit button.
# We use a variable that is true unless the user presses the quit button.
#  To keep the game running we use a while loop and check our variable if it is true or not.

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
