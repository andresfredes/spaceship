from pathlib import Path

from pygame.image import load
from pygame.surface import Surface

from src.models.mixin import DrawMixin
from src.settings import settings
from src.type import Position


class Ship(DrawMixin):
    @property
    def surface(self) -> Surface:
        return self._surface

    @property
    def pos(self) -> Position:
        return self._pos

    def __init__(self):
        self._pos: Position = [200, 50]
        self._ship_filename = Path(settings.ASSETS_DIR / "ship" / "ship_test.png")
        self._surface = load(self._ship_filename)
