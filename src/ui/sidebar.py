import pygame
import pygame_gui
from .elements import *
from .colors import *


class Sidebar:
    def __init__(self, p_game: pygame, gui_manager: pygame_gui) -> None:
        self.p_game = p_game
        self.gui_manager = gui_manager

        self.surface = self._create_surface()
        self.test_button = create_button(
            self.gui_manager, (25, 50), (100, 50), "Button"
        )

    def _create_surface(self) -> pygame.surface:
        display_info = self.p_game.display.Info()
        width = display_info.current_w * 0.2
        height = display_info.current_h

        surface = self.p_game.Surface((width, height))
        surface.fill(LIGHT_GREY)
        return surface

    def handle_input(self, game_event: pygame.Event) -> None:
        handle_button_event(
            button=self.test_button,
            game_event=game_event,
            button_event=pygame_gui.UI_BUTTON_PRESSED,
            callback=lambda: print("hello world"),
        )

    def draw(self) -> None:
        display = self.p_game.display.get_surface()
        display.blit(self.surface, (0, 0))
