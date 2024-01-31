import pygame
import pygame_gui
from .colorpicker import ColorPicker


class Sidebar:
    def __init__(self, p_game: pygame, gui_manager: pygame_gui) -> None:
        self.p_game = p_game
        self.gui_manager = gui_manager
        self.surface = self._create_surface()
        button_x = self.surface.get_width() * 0.125

        self.menu_title = pygame_gui.elements.UILabel(
            manager=gui_manager,
            relative_rect=pygame.Rect((10, 10), (-1, -1)),
            text="Sorting Algorithm Visualizer",
        )

        self.bar_color_picker = ColorPicker(
            gui_manager=gui_manager,
            location=(button_x, 50),
            text="Bar",
            tooltip_text="Change Bar Color",
            default_color=(255, 255, 255),
        )
        self.background_color_picker = ColorPicker(
            gui_manager=gui_manager,
            location=(button_x, 120),
            text="Background",
            tooltip_text="Change Background Color",
            default_color=(0, 0, 0),
        )

    def _create_surface(self) -> pygame.surface:
        display_info = self.p_game.display.Info()
        width = display_info.current_w * 0.3
        height = display_info.current_h

        surface = self.p_game.Surface((width, height))
        surface.fill("grey")
        return surface

    def handle_input(self, event: pygame.Event) -> None:
        self.bar_color_picker.run(event, "Change Bar Color")

        self.background_color_picker.run(event, "Change Background Color")
        if (
            event.type == pygame_gui.UI_COLOUR_PICKER_COLOUR_PICKED
            and event.ui_element == self.background_color_picker.color_picker_dialog
        ):
            print("background change color")

    def draw(self) -> None:
        display = self.p_game.display.get_surface()
        display.blit(self.surface, (0, 0))
        self.bar_color_picker.draw(display)
        self.background_color_picker.draw(display)
