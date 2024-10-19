from pygame.freetype import SysFont, get_default_font
from pygame.rect import Rect
from pygame.surface import Surface

from src.enums import Colour
from src.models.mixin import DrawMixin, MouseMixin, set_bounds
from src.settings import settings
from src.type import Position


class Enemy(DrawMixin, MouseMixin):
    @property
    def surface(self) -> Surface:
        return self._surface

    @property
    def pos(self) -> Position:
        return self._pos

    @property
    def bounds(self) -> Rect:
        return self._bounds

    def __init__(self, pos: Position = (0, 0), name: str = ""):
        self._pos: Position = pos
        self._width: int = settings.BATTLE_SHIP_WIDTH
        self._height: int = settings.BATTLE_SHIP_HEIGHT
        self._colour: Colour = Colour.WHITE.value

        self.name: str = name
        self._name_pos: Position = (10, 10)
        self._name_colour: Colour = Colour.BLACK.value
        self._font = SysFont(get_default_font(), settings.FONT_SIZE)

        self.resurface()
        self._bounds: Rect = set_bounds(bounds=self._surface.get_rect(), pos=self._pos)

    def resurface(self, /, show_name=False):
        self._surface: Surface = Surface((self._width, self._height)).convert()
        self._surface.fill(self._colour)
        if show_name:
            self._font.render_to(
                surf=self._surface,
                dest=self._name_pos,
                text=self.name,
                fgcolor=self._name_colour,
            )

    def on_hover(self, _):
        self.resurface(show_name=True)

    def off_hover(self, _):
        self.resurface(show_name=False)
