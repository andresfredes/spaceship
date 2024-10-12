from random import randint

from pygame.display import flip, set_mode
from pygame.draw import line
from pygame.surface import Surface
from pygame.time import Clock

from src.colours import Colour
from src.models.components import DrawMixin
from src.settings import settings
from src.state import state


class Renderer:
    def __init__(self):
        self.screen = set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        self.background = Surface(self.screen.get_size()).convert()
        self.stars = [
            [randint(0, settings.SCREEN_WIDTH), randint(0, settings.SCREEN_HEIGHT)]
            for _ in range(settings.NUM_STARS)
        ]
        self.clock = Clock()

    def render_frame(self):
        self.background.fill(Colour.BLACK.value)

        for star in self.stars:
            line(self.background, Colour.WHITE.value, star, star)
            star[0] = star[0] - 1
            if star[0] < 0:
                star[0] = settings.SCREEN_WIDTH
                star[1] = randint(0, settings.SCREEN_HEIGHT)

        for collection in state.current:
            for item in collection:
                if not isinstance(item, DrawMixin):
                    continue
                item.draw(self.background)

        self.screen.blit(self.background, (0, 0))
        flip()
        self.clock.tick(60)
