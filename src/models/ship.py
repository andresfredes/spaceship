from pathlib import Path

import pygame

from src.models.components import DrawMixin
from src.models.types import Position
from src.settings import settings


class Ship(DrawMixin):
    @property
    def surface(self):
        return self._surface

    @property
    def pos(self) -> Position:
        return self._pos

    def __init__(self):
        self._pos: Position = [200, 50]
        self._ship_filename = Path(settings.ASSETS_DIR / "ship" / "ship_test.png")
        self._surface = pygame.image.load(self._ship_filename)
