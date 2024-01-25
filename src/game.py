import pygame, pygame_gui, os
from sys import exit
from .ui.sidebar import Sidebar

# Constants
WINDOW_TITLE = "Sorting Algorithm Visualizer"
DEFAULT_DISPLAY_SIZE = (800, 600)
DEFAULT_BACKGROUND_COLOR = "black"
FRAME_RATE = 60
THEME_PATH = f"{os.path.dirname(os.path.realpath(__file__))}\\ui\\theme.json"


class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption(WINDOW_TITLE)

        # Initialize Pygame and set window title
        self.display = pygame.display.set_mode(DEFAULT_DISPLAY_SIZE, pygame.RESIZABLE)
        self.gui_manager = pygame_gui.UIManager(DEFAULT_DISPLAY_SIZE, THEME_PATH)
        self.clock = pygame.time.Clock()

        # Create background surface
        self.background = self._create_background(
            DEFAULT_DISPLAY_SIZE, DEFAULT_BACKGROUND_COLOR
        )

        # Load sidebar menu
        self.sidebar = Sidebar(pygame, self.gui_manager)

    # Start game loop
    def start(self) -> None:
        while True:
            self._handle_input()
            self._game_logic()
            self._draw()
        pygame.quit()

    def _create_background(self, size: tuple, color: tuple) -> pygame.Surface:
        background = pygame.Surface(size)
        background.fill(color)
        return background

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
        self.display.blit(self.background, (0, 0))

        self.sidebar.draw()

        self.gui_manager.draw_ui(self.display)
        pygame.display.update()
