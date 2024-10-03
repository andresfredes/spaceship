import pygame
import pygame.freetype

from src.colours import Colour
from src.models.components import BaseObject, DrawMixin, MouseMixin
from src.settings import settings


class Card(BaseObject, DrawMixin, MouseMixin):
    def __init__(self, pos=[0, 0], title="", text=""):
        self._pos = pos
        self._title = title
        self._text = text

        self._width = settings.CARD_WIDTH
        self._height = settings.CARD_HEIGHT
        self._colour = Colour.WHITE.value
        self._text_colour = Colour.BLACK.value

        self._font = pygame.freetype.SysFont(
            pygame.freetype.get_default_font(), settings.FONT_SIZE
        )
        self._surface = pygame.Surface((self._width, self._height)).convert()
        self._bounds = self._surface.get_rect()
        self.mouse_move((0, 0), init_override=True)

        self._surface.fill(self._colour)
        self._font.render_to(
            surf=self._surface,
            dest=(10, 10),
            text=self._title,
            fgcolor=self._text_colour,
        )
        self._font.render_to(
            surf=self._surface,
            dest=(10, 100),
            text=self._text,
            fgcolor=self._text_colour,
        )
