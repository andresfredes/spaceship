from collections.abc import Callable

from pygame.freetype import SysFont, get_default_font
from pygame.rect import Rect
from pygame.surface import Surface

from src.enums import Colour
from src.models.mixin import DrawMixin, MouseMixin, set_bounds
from src.settings import settings
from src.type import Position


class Button(DrawMixin, MouseMixin):
    @property
    def surface(self) -> Surface:
        return self._surface

    @property
    def pos(self) -> Position:
        return self._pos

    @property
    def bounds(self) -> Rect:
        return self._bounds

    def __init__(
        self, pos: Position = [0, 0], text: str = "", action: Callable | None = None
    ):
        self._pos: Position = pos
        self._text: str = text
        self._action: Callable = action

        self._width: int = settings.BUTTON_WIDTH
        self._height: int = settings.BUTTON_HEIGHT
        self._colour: Colour = Colour.WHITE.value
        self._hover_colour: Colour = Colour.BLUE.value
        self._text_colour: Colour = Colour.BLACK.value
        self._text_pos: Position = (70, 40)
        self._font = SysFont(get_default_font(), settings.FONT_SIZE)
        self.resurface()
        self._bounds: Rect = set_bounds(bounds=self._surface.get_rect(), pos=self._pos)

    def resurface(self, /, colour=None) -> Surface:
        self._surface = Surface((self._width, self._height)).convert()
        self._surface.fill(self._colour if colour is None else colour)
        self._font.render_to(
            surf=self._surface,
            dest=self._text_pos,
            text=self._text,
            fgcolor=self._text_colour,
        )

    def on_hover(self, _) -> None:
        self.resurface(colour=self._hover_colour)

    def off_hover(self, _) -> None:
        self.resurface(colour=self._colour)

    def on_mouse_down(self, _) -> None:
        pass

    def on_mouse_up(self, _) -> None:
        if self._action is not None:
            self._action()
