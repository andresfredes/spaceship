import pygame

from src.models.components import MouseMixin
from src.settings import settings
from src.state import state


class EventHandler:
    def step(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            for obj in state.objects:
                if isinstance(obj, MouseMixin):
                    if (
                        event.type == pygame.MOUSEBUTTONDOWN
                        and event.button == settings.LEFT_CLICK
                    ):
                        obj.click_down(event.pos)
                    if (
                        event.type == pygame.MOUSEBUTTONUP
                        and event.button == settings.LEFT_CLICK
                    ):
                        obj.click_up(event.pos)
                    if event.type == pygame.MOUSEMOTION:
                        obj.mouse_move(event.rel)
                    if event.type == pygame.MOUSEMOTION:
                        obj.hover(event.pos)
        return True
