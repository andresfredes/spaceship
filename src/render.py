from random import randint

import pygame

from src.colours import Colour
from src.settings import settings
from src.state import state
from src.view import View


class Renderer:
    def __init__(self):
        self.screen = pygame.display.set_mode(
            (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)
        )
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.stars = [
            [randint(0, settings.SCREEN_WIDTH), randint(0, settings.SCREEN_HEIGHT)]
            for _ in range(settings.NUM_STARS)
        ]
        self.clock = pygame.time.Clock()

    def render_frame(self):
        self.background.fill(Colour.BLACK.value)

        for star in self.stars:
            pygame.draw.line(self.background, Colour.WHITE.value, star, star)
            star[0] = star[0] - 1
            if star[0] < 0:
                star[0] = settings.SCREEN_WIDTH
                star[1] = randint(0, settings.SCREEN_HEIGHT)

        match state.view:
            case View.MENU:
                pass
            case View.SHIP:
                state.ship.draw(self.background)
            case View.BATTLE:
                state.hand.draw(self.background)
            case _:
                pass

        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()
        self.clock.tick(60)
