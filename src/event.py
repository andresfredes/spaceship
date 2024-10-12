import pygame
from pygame.event import Event

from src.models.components import MouseMixin, MouseMoveMixin
from src.settings import settings
from src.state import state


class EventHandler:
    def step(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            self.handle_event(event)
        return True

    def handle_event(self, event: Event):
        for collection in state.current:
            for item in collection:
                if not isinstance(item, MouseMixin):
                    continue
                if (
                    event.type == pygame.MOUSEBUTTONDOWN
                    and event.button == settings.LEFT_CLICK
                ):
                    item.click_down(event.pos)
                if (
                    event.type == pygame.MOUSEBUTTONUP
                    and event.button == settings.LEFT_CLICK
                ):
                    item.click_up(event.pos)
                if event.type == pygame.MOUSEMOTION:
                    item.hover(event.pos)
                    if isinstance(item, MouseMoveMixin):
                        item.mouse_move(event.rel)
