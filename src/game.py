import pygame
import pygame_gui
from sys import exit
from .sidebar import Sidebar

# Constants
WINDOW_TITLE = "Sorting Algorithm Visualizer"
DEFAULT_DISPLAY_SIZE = (800, 600)
FRAME_RATE = 60


class Game:
    # Initialize Pygame and set window title
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption(WINDOW_TITLE)

        self.display = pygame.display.set_mode(DEFAULT_DISPLAY_SIZE, pygame.RESIZABLE)
        self.gui_manager = pygame_gui.UIManager(DEFAULT_DISPLAY_SIZE)
        self.clock = pygame.time.Clock()

        self.sidebar = Sidebar(pygame, self.gui_manager)

    # Start game loop
    def start(self) -> None:
        while True:
            self._handle_input()
            self._game_logic()
            self._draw()

    # Handle user input and I/O
    def _handle_input(self) -> None:
        time_delta = self.clock.tick(FRAME_RATE) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            self.sidebar.handle_input(event)

            self.gui_manager.process_events(event)
        self.gui_manager.update(time_delta)

    # Where sorting algorithm logic goes
    def _game_logic(self) -> None:
        pass

    # Updates display ever frame
    def _draw(self) -> None:
        self.sidebar.draw()
        self.gui_manager.draw_ui(self.display)
        pygame.display.update()
