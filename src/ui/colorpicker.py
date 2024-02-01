import pygame, pygame_gui


# Constants
PICK_COLOR_BUTTON_SIZE = (110, 50)
PICKED_COLOR_BOX_SIZE = (50, 50)


class ColorPicker:
    def __init__(
        self,
        gui_manager: pygame_gui,
        location: tuple = (0, 0),
        size: tuple = PICK_COLOR_BUTTON_SIZE,
        text: str = "",
        tooltip_text: str = "",
        anchors: dict[str, str] = None,
        default_color: tuple = (255, 255, 255),
    ) -> None:
        self._gui_manager = gui_manager
        self.current_color = pygame.Color(default_color)

        # Create button to display color picker dialog
        self.pick_color_button = pygame_gui.elements.UIButton(
            manager=gui_manager,
            relative_rect=pygame.Rect(location, size),
            text=text,
            tool_tip_text=tooltip_text,
            anchors=anchors,
        )
        self.color_picker_dialog = None

        # Create box to display picked color
        self.picked_color_box = pygame.Surface(PICKED_COLOR_BOX_SIZE)
        self.picked_color_box.fill(self.current_color)
        self.picked_color_box_location = location

    def run(
        self,
        event: pygame.Event,
        window_title: str,
    ) -> None:
        # When a user clicks on the change color button
        if (
            event.type == pygame_gui.UI_BUTTON_PRESSED
            and event.ui_element == self.pick_color_button
        ):
            self.color_picker_dialog = pygame_gui.windows.UIColourPickerDialog(
                manager=self._gui_manager,
                rect=pygame.Rect((50, 50), (390, 390)),
                window_title=window_title,
                initial_colour=self.current_color,
            )
            self.pick_color_button.disable()

        # When a user chooses a color and clicks "ok" on the color picker dialog
        if (
            event.type == pygame_gui.UI_COLOUR_PICKER_COLOUR_PICKED
            and event.ui_element == self.color_picker_dialog
        ):
            self.current_color = event.colour
            self.picked_color_box.fill(self.current_color)

        # When a user closes the color picker dialog
        if (
            event.type == pygame_gui.UI_WINDOW_CLOSE
            and event.ui_element == self.color_picker_dialog
        ):
            self.pick_color_button.enable()
            self.color_picker_dialog = None

    def draw(self, display: any) -> None:
        x = self.picked_color_box_location[0]
        y = self.picked_color_box_location[1]
        location = (x + (PICKED_COLOR_BOX_SIZE[0] * 2) + 20, y)

        display.blit(self.picked_color_box, location)
