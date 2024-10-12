from collections.abc import Callable

from pygame.freetype import SysFont, get_default_font
from pygame.surface import Surface

from src.colours import Colour
from src.models.components import DrawMixin, MouseMixin
from src.models.types import Position
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


class Button(DrawMixin, MouseMixin):
    @property
    def surface(self):
        return self._surface

    @property
    def pos(self) -> Position:
        return self._pos

    @property
    def bounds(self):
        return self._bounds

    def __init__(
        self, pos: Position = [0, 0], text: str = "", action: Callable | None = None
    ):
        self._pos = pos
        self._text: str = text
        self._action = action

        self._width = settings.BUTTON_WIDTH
        self._height = settings.BUTTON_HEIGHT
        self._colour = Colour.WHITE.value
        self._text_colour = Colour.BLACK.value

        self._font = SysFont(get_default_font(), settings.FONT_SIZE)
        self._surface = Surface((self._width, self._height)).convert()
        self._bounds = self._bounds = self._surface.get_rect()

        self._surface.fill(self._colour)
        self._font.render_to(
            surf=self._surface,
            dest=(70, 40),
            text=self._text,
            fgcolor=self._text_colour,
        )

    def on_hover(self, _):
        self._colour = Colour.RED.value

    def on_mouse_down(self, _):
        self._colour = Colour.BLUE.value

    def on_mouse_up(self, _):
        self._colour = Colour.WHITE.value
        if self._action is not None:
            self._action()
