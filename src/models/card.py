from pygame.freetype import SysFont, get_default_font
from pygame.rect import Rect
from pygame.surface import Surface

from src.enums import Colour
from src.models.mixin import DrawMixin, MouseMixin, MouseMoveMixin, set_bounds
from src.settings import settings
from src.type import Position


class Card(DrawMixin, MouseMixin, MouseMoveMixin):
    @property
    def surface(self) -> Surface:
        return self._surface

    @property
    def bounds(self) -> Rect:
        return self._bounds

    @property
    def pos(self) -> Position:
        return self._pos

    @pos.setter
    def pos(self, val: Position):
        self._pos = val

    def __init__(self, pos: Position = [0, 0], title: str = "", text: str = ""):
        self._pos: Position = pos
        self._title: str = title
        self._text: str = text

        self._width: int = settings.CARD_WIDTH
        self._height: int = settings.CARD_HEIGHT
        self._colour: Colour = Colour.WHITE.value
        self._text_colour: Colour = Colour.BLACK.value

        self._font = SysFont(get_default_font(), settings.FONT_SIZE)
        self._surface: Surface = Surface((self._width, self._height)).convert()
        self._bounds: Rect = set_bounds(bounds=self._surface.get_rect(), pos=self._pos)

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

    def __repr__(self):
        return f"{self.__class__.__name__} ({self._title})"
