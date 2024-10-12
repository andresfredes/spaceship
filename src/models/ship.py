from pathlib import Path

from pygame.image import load
from pygame.surface import Surface

from src.models.components import DrawMixin
from src.models.types import Position
from src.settings import settings


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
