import os
from pathlib import Path


class Settings:
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720

    NUM_STARS = 150

    CARD_WIDTH = 150
    CARD_HEIGHT = 200

    FONT_SIZE = 12

    ROOT_DIR = Path(os.path.dirname(os.path.abspath(__file__))).parent
    ASSETS_DIR = Path(ROOT_DIR / "assets")

    BUTTON_WIDTH = 200
    BUTTON_HEIGHT = 100


settings = Settings()
