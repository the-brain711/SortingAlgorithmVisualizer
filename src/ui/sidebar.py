import pygame
import pygame_gui
from .colorpicker import ColorPicker
from .colors import *


class Sidebar:
    def __init__(self, p_game: pygame, gui_manager: pygame_gui) -> None:
        self.p_game = p_game
        self.gui_manager = gui_manager
        self.surface = self._create_surface()

        self.color_picker = ColorPicker(
            gui_manager=gui_manager, location=(10, 10), size=(100, 50), text="Bar Color"
        )

    def _create_surface(self) -> pygame.surface:
        display_info = self.p_game.display.Info()
        width = display_info.current_w * 0.3
        height = display_info.current_h

        surface = self.p_game.Surface((width, height))
        surface.fill(LIGHT_GREY)
        return surface

    def handle_input(self, event: pygame.Event) -> None:
        self.color_picker.handle_color_picker_events(event, "Change Bar Color")

    def draw(self) -> None:
        display = self.p_game.display.get_surface()
        display.blit(self.surface, (0, 0))
        self.color_picker.draw(display)
