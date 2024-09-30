import pygame
import pygame.freetype

from src.colours import Colour
from src.settings import settings


class Menu:
    def __init__(self, buttons=[]):
        self._buttons = buttons

    def __iter__(self):
        for button in self._buttons:
            yield button

    def click(self, pos):
        for button in self._buttons:
            if button.collidepoint(pos):
                button._action()


class Button:
    def __init__(self, pos=[0, 0], text="", action=None):
        # TODO: placeholder - will eventually be an image
        self._pos = pos
        self._text = text
        self._action = action

        self._width = settings.BUTTON_WIDTH
        self._height = settings.BUTTON_HEIGHT
        self._colour = Colour.WHITE.value
        self._text_colour = Colour.BLACK.value

        self._font = pygame.freetype.SysFont(
            pygame.freetype.get_default_font(), settings.FONT_SIZE
        )
        self._surface = pygame.Surface((self._width, self._height)).convert()
        self._bounds = self._bounds = self._surface.get_rect()

        self._surface.fill(self._colour)
        self._font.render_to(
            surf=self._surface,
            dest=(70, 40),
            text=self._text,
            fgcolor=self._text_colour,
        )

    def collidepoint(self, pos):
        return self._bounds.collidepoint(pos)

    def draw(self, surface):
        surface.blit(self._surface, self._pos)
