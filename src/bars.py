import pygame, random


class Bars:
    def __init__(self, p_game: pygame, surface: pygame.Surface) -> None:
        self._pygame = p_game
        self._surface = surface
        self._width = surface.get_width()
        self._height = surface.get_height()

    # Generates a random list of integers to be sorted
    def generate_bars_list(self, bar_count: int) -> list[int]:
        max_bar_height = self._height - 100
        random.seed()
        return [random.randint(10, max_bar_height) for i in range(bar_count)]

    def draw(self, bars_list: list[int], color: tuple) -> None:
        bar_count = len(bars_list)
        side_padding = 10
        bar_space = 1

        for i, bar_height in enumerate(bars_list):
            location_x = i * ((self._width - (side_padding * 2)) / bar_count)
            location_y = self._height - bar_height
            bar_width = ((self._width - (side_padding * 2)) / bar_count) - bar_space

            if i == 0:
                location_x = (self._width - (side_padding * 2)) / bar_count
                pygame.draw.rect(
                    surface=self._surface,
                    color=color,
                    rect=(location_x, location_y, bar_width, bar_height),
                )
            else:
                pygame.draw.rect(
                    surface=self._surface,
                    color=color,
                    rect=(location_x, location_y, bar_width, bar_height),
                )
