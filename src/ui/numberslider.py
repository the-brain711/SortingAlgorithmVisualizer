import pygame, pygame_gui

# Constants
SLIDER_SIZE = (175, 50)


class NumberSlider:
    def __init__(
        self,
        gui_manager: pygame_gui,
        title_label: str,
        location: tuple = (0, 0),
        size: tuple = SLIDER_SIZE,
        value_range: tuple = (10, 100),
        start_value: int = 25,
        click_increment: int = 1,
    ) -> None:
        self._gui_manager = gui_manager

        self.title_label = pygame_gui.elements.UILabel(
            manager=gui_manager,
            relative_rect=pygame.Rect((location[0], location[1]), (-1, -1)),
            text=title_label,
            object_id=pygame_gui.core.ObjectID(
                class_id="@title", object_id=f"#{title_label}"
            ),
        )

        self.slider_value_label = pygame_gui.elements.UILabel(
            manager=gui_manager,
            relative_rect=pygame.Rect(((size[0] / 2) + 30, location[1]), (-1, -1)),
            text=str(start_value),
        )

        self.slider = pygame_gui.elements.UIHorizontalSlider(
            manager=gui_manager,
            relative_rect=pygame.Rect((location[0], location[1] + 25), size),
            value_range=value_range,
            start_value=start_value,
            click_increment=click_increment,
        )

    def run(self, event: pygame.Event) -> None:
        if (
            event.type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED
            and event.ui_element == self.slider
        ):
            self.slider_value_label.set_text(str(event.value))
