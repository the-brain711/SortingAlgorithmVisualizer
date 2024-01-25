import pygame
import pygame_gui
from .colorpicker import ColorPicker
from .numberslider import NumberSlider


class Sidebar:
    def __init__(self, p_game: pygame, gui_manager: pygame_gui) -> None:
        self._pygame = p_game
        self._gui_manager = gui_manager

        # Create background for sidebar
        self._surface = self._create_surface()
        self._center_x = self._surface.get_width() * 0.125

        # Create color pickers to change colors of bars and background
        self._create_color_pickers()

        # Create dropdown to pick which sorting algorithm to choose
        self._create_dropdown()

        # Create slider to control how many bars will be used by the sorting algorithm
        self.number_slider = NumberSlider(
            gui_manager=gui_manager,
            title_label="Bar Count:",
            location=(self._center_x, 300),
        )

        # Create start and generate buttons
        self._create_buttons()

    def _create_surface(self) -> pygame.surface:
        display_info = self._pygame.display.Info()
        width = display_info.current_w * 0.3
        height = display_info.current_h

        surface = self._pygame.Surface((width, height))
        surface.fill("grey")
        return surface

    # Create color pickers for sidebar
    def _create_color_pickers(self) -> None:
        self.color_pickers_title = pygame_gui.elements.UILabel(
            manager=self._gui_manager,
            relative_rect=pygame.Rect((self._center_x, 20), (-1, -1)),
            text="Color Pickers",
            object_id=pygame_gui.core.ObjectID(
                class_id="@title", object_id="#color_pickers_title"
            ),
        )

        self.bar_color_picker = ColorPicker(
            gui_manager=self._gui_manager,
            location=(self._center_x, 50),
            text="Bar",
            tooltip_text="Change Bar Color",
            default_color=(255, 255, 255),
        )

        self.background_color_picker = ColorPicker(
            gui_manager=self._gui_manager,
            location=(self._center_x, 110),
            text="Background",
            tooltip_text="Change Background Color",
            default_color=(0, 0, 0),
        )

    def _create_dropdown(self) -> None:
        self.dropdown_title = pygame_gui.elements.UILabel(
            manager=self._gui_manager,
            relative_rect=pygame.Rect((self._center_x, 190), (-1, -1)),
            text="Sorting Algorithms",
            object_id=pygame_gui.core.ObjectID(
                class_id="@title", object_id="#dropdown_title"
            ),
        )

        self.sorting_algorithm_dropdown = pygame_gui.elements.UIDropDownMenu(
            manager=self._gui_manager,
            relative_rect=pygame.Rect((self._center_x, 220), (175, 50)),
            starting_option="Bubble Sort",
            options_list=["Bubble Sort", "Merge Sort", "Quick Sort"],
        )

    def _create_buttons(self) -> None:
        self.generate_button = pygame_gui.elements.UIButton(
            manager=self._gui_manager,
            relative_rect=pygame.Rect((self._center_x + 30, 420), (110, 50)),
            text="Generate",
            tool_tip_text="Generate New Bars",
        )

        self.start_button = pygame_gui.elements.UIButton(
            manager=self._gui_manager,
            relative_rect=pygame.Rect((self._center_x + 30, 480), (110, 50)),
            text="Start",
            tool_tip_text="Start Sorting Bars",
        )

    def handle_input(self, event: pygame.Event) -> None:
        self.bar_color_picker.run(event, "Change Bar Color")

        self.background_color_picker.run(event, "Change Background Color")
        if (
            event.type == pygame_gui.UI_COLOUR_PICKER_COLOUR_PICKED
            and event.ui_element == self.background_color_picker.color_picker_dialog
        ):
            print(
                f"background change color: {self.background_color_picker.current_color}"
            )

        self.number_slider.run(event)

    def draw(self) -> None:
        display = self._pygame.display.get_surface()
        display.blit(self._surface, (0, 0))
        self.bar_color_picker.draw(display)
        self.background_color_picker.draw(display)
