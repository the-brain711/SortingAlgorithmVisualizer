import pygame
from sys import exit

# Constants
DEFAULT_DISPLAY_SIZE = (800, 600)
FRAME_RATE = 60

pygame.init()
display = pygame.display.set_mode(DEFAULT_DISPLAY_SIZE, pygame.RESIZABLE)
pygame.display.set_caption("Sorting Algorithmn Visualizer")
clock = pygame.time.Clock()

while True:
    # Handle closing the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Draw elements here

    # Updates display ever frame
    pygame.display.update()
    clock.tick(FRAME_RATE)
