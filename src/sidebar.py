import pygame
import pygame_gui
from .colors import *


class Sidebar:
    def __init__(self, p_game: pygame, gui_manager: pygame_gui) -> None:
        self.p_game = p_game
        self.gui_manager = gui_manager

        self.surface = self._create_surface()
        self.test_button = self._create_button((25, 50), (100, 50), "Button")

    def _create_surface(self) -> pygame.surface:
        display_info = self.p_game.display.Info()
        width = display_info.current_w * 0.2
        height = display_info.current_h

        surface = self.p_game.Surface((width, height))
        surface.fill(LIGHT_GREY)
        return surface

    def _create_button(
        self, location: tuple, size: tuple, text: str
    ) -> pygame_gui.elements.UIButton:
        return pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(location, size),
            text=text,
            manager=self.gui_manager,
        )

    def handle_input(self, event: pygame.Event) -> None:
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.test_button:
                print("hello world")

    def draw(self) -> None:
        display = self.p_game.display.get_surface()
        display.blit(self.surface, (0, 0))
