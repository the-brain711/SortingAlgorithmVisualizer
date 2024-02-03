import pygame, random


class Bars:
    def __init__(self, p_game: pygame, surface: pygame.Surface) -> None:
        self._pygame = p_game
        self._surface = surface
        self._width = surface.get_width()
        self._height = surface.get_height()

        self.bars_list = []

    def generate(self, color: tuple, bar_count: int) -> None:
        self.bars_list.clear()
        location_x = 0
        width = round(20 - (bar_count * 0.2))

        while bar_count > 0:
            random.seed(bar_count)

            if location_x >= self._surface.get_width():
                location_x = self._surface.get_width() - 25
            else:
                location_x += width + 1

            random_height = random.randint(50, 600)
            location_y = 610 - random_height

            bar = self._pygame.draw.rect(
                surface=self._surface,
                color=color,
                rect=pygame.Rect(location_x, location_y, width, random_height),
            )
            self.bars_list.append(bar)
            bar_count -= 1
