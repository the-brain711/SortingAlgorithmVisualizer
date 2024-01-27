import pygame
import pygame_gui
from .colors import *


def create_button(
    gui_manager: pygame_gui, location: tuple, size: tuple, text: str
) -> pygame_gui.elements.UIButton:
    return pygame_gui.elements.UIButton(
        manager=gui_manager, relative_rect=pygame.Rect(location, size), text=text
    )


def handle_button_event(
    button: pygame_gui.elements.UIButton,
    game_event: pygame.Event,
    button_event: int,
    callback: lambda x: x,
):
    if game_event.type == button_event:
        if game_event.ui_element == button:
            callback()
