import pygame
import pygame_gui
from sys import exit

# Constants
DEFAULT_DISPLAY_SIZE = (800, 600)
DEFAULT_SIDEBAR_SIZE = (DEFAULT_DISPLAY_SIZE[0] * 0.2, DEFAULT_DISPLAY_SIZE[1])
FRAME_RATE = 60
LIGHT_GREY = (220, 220, 220)

pygame.init()
display = pygame.display.set_mode(DEFAULT_DISPLAY_SIZE, pygame.RESIZABLE)
pygame.display.set_caption("Sorting Algorithmn Visualizer")
clock = pygame.time.Clock()

left_sidebar_surface = pygame.Surface(DEFAULT_SIDEBAR_SIZE)
left_sidebar_surface.fill(LIGHT_GREY)

gui_manager = pygame_gui.UIManager(DEFAULT_DISPLAY_SIZE)

button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((0, 0), (100, 50)), text="Hello", manager=gui_manager
)

while True:
    time_delta = clock.tick(FRAME_RATE) / 1000.0

    for event in pygame.event.get():
        # Handle closing the window
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == button:
                print("hello world")

        gui_manager.process_events(event)

    gui_manager.update(time_delta)

    # Draw elements here
    display.blit(left_sidebar_surface, (0, 0))
    gui_manager.draw_ui(display)

    # Updates display ever frame
    pygame.display.update()
