import pygame, pygame_gui, os
from sys import exit
from .ui.sidebar import Sidebar
from .bars import Bars
from .sorting_algorithm import SortingAlgorithm

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
        self._display = pygame.display.set_mode(DEFAULT_DISPLAY_SIZE, pygame.RESIZABLE)
        self._gui_manager = pygame_gui.UIManager(DEFAULT_DISPLAY_SIZE, THEME_PATH)
        self._clock = pygame.time.Clock()

        # Create surface background for entire program
        self._background_surface = self._create_surface()

        # Create surface to draw bars on
        self._bar_surface = self._create_surface(
            size=(self._display.get_width() * 0.7, self._display.get_height())
        )
        self._bars_list = []
        self._bars = Bars(pygame, self._bar_surface)

        # Load sidebar menu
        self._sidebar = Sidebar(pygame, self._gui_manager)

        # Load sorting algorithm class to sort bars
        # self._sorting_algorithm = SortingAlgorithm(pygame)

    # Start game loop
    def start(self) -> None:
        while True:
            self._handle_input()
            self._game_logic()
            self._draw()

    def _create_surface(
        self,
        size: tuple = DEFAULT_DISPLAY_SIZE,
        color: tuple = DEFAULT_BACKGROUND_COLOR,
    ) -> pygame.Surface:
        background = pygame.Surface(size)
        background.fill(color)
        return background

    # Handle user input and I/O
    def _handle_input(self) -> None:
        time_delta = self._clock.tick(FRAME_RATE) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            self._sidebar.handle_input(event)

            # Change bar color when user selects new color from color dialog
            self._change_bar_color_event(event)

            # Change background color when user selects new color from color dialog
            self._change_background_color_event(event)

            # Generates new set of bars for sorting when generate/reset button is clicked
            self._generate_bars_event(event)

            self._gui_manager.process_events(event)
        self._gui_manager.update(time_delta)

    def _change_bar_color_event(self, event: pygame.Event):
        bar_color_picker = self._sidebar.bar_color_picker

        if (
            event.type == pygame_gui.UI_COLOUR_PICKER_COLOUR_PICKED
            and event.ui_element == bar_color_picker.color_picker_dialog
            and self._bars_list != None
            and self._bars_list != 0
        ):
            # Redraw entire screen and then redraw bars
            background_color = self._sidebar.background_color_picker.current_color
            bar_color = bar_color_picker.current_color

            self._bar_surface.fill(background_color)
            self._bars.draw(self._bars_list, bar_color)

    def _change_background_color_event(self, event: pygame.Event) -> None:
        background_color_picker = self._sidebar.background_color_picker

        if (
            event.type == pygame_gui.UI_COLOUR_PICKER_COLOUR_PICKED
            and event.ui_element == background_color_picker.color_picker_dialog
        ):
            # Redraw entire screen with new background color and then redraw bars
            self._bar_surface.fill(background_color_picker.current_color)
            if self._bars_list != None or len(self._bars_list) != 0:
                color = self._sidebar.bar_color_picker.current_color
                self._bars.draw(self._bars_list, color)

    def _generate_bars_event(self, event: pygame.Event) -> None:
        if (
            event.type == pygame_gui.UI_BUTTON_PRESSED
            and event.ui_element == self._sidebar.generate_button
        ):
            background_color = self._sidebar.background_color_picker.current_color
            self._bar_surface.fill(background_color)

            bar_count = self._sidebar.number_slider.slider.get_current_value()
            bar_color = self._sidebar.bar_color_picker.current_color

            self._bars_list = self._bars.generate_bars_list(bar_count)
            self._bars.draw(self._bars_list, bar_color)

    # Where sorting algorithm logic goes
    def _game_logic(self) -> None:
        pass

    # Updates display ever frame
    def _draw(self) -> None:
        # Draw background and bar surface
        self._display.blit(self._background_surface, (0, 0))
        self._display.blit(self._bar_surface, (self._display.get_width() * 0.3, 0))

        # Draw sidebar menu
        self._sidebar.draw(self._display)

        self._gui_manager.draw_ui(self._display)
        pygame.display.update()
