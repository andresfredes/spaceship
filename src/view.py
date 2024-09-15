from enum import Enum
from pathlib import Path

import pygame

from src.settings import settings


class View(Enum):
    MENU = 0
    SHIP = 1
    BATTLE = 2


class Ship:
    def __init__(self):
        self._ship_filename = Path(settings.ASSETS_DIR / "ship" / "ship_test.png")
        self._surface = pygame.image.load(self._ship_filename)

    def draw(self, surface):
        surface.blit(self._surface, [200, 50])
