
# This function works the same as pygame.time.wait function
#  the difference is that this function will use the processor(rather than sleeping)
# in order to make the delay more accurate.
#  The sample code can be written the same as pygame.time.wait function by just replacing the name:

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400, 500), pygame.RESIZABLE)
color = "yellow"

# delaying of time 2 sec
pygame.time.delay(2000)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(color)
    pygame.display.flip()
