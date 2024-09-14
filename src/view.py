from enum import Enum

from src.settings import settings


class View(Enum):
    MENU = 0
    SHIP = 1
    BATTLE = 2


class Ship:
    def __init__(self):
        print(settings.ROOT_DIR)
        # self._surface =

    def draw(self):
        pass
